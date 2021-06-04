from flask import Flask, request, abort, jsonify, Response
import FinanceDataReader as fdr
from pykrx import stock
from datetime import date, timedelta

app = Flask(__name__)


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/api/v1/stock/code')
def getListedStockCodes():
    type = request.args.get('type')
    if type not in ['KRX', 'NASDAQ']:
        abort(400, 'Bad Type')

    if type == 'KRX':
        return jsonify(getKrxCodes())

    df = fdr.StockListing('NASDAQ')[['Symbol', 'Name']]
    return Response(df.to_json(orient='records'), mimetype='application/json')


def getKrxCodes():
    result = []
    for ticker in stock.get_market_ticker_list(market='ALL'):
        name = stock.get_market_ticker_name(ticker)
        result.append({
            "Symbol": ticker,
            "Name": name
        })
    return result


@app.route('/api/v1/stock/price')
def getCurrentStockPrice():
    codes = request.args.get('codes')
    codes = distinctAndSplit(codes)
    result = []
    day = date.today() - timedelta(days=14)
    for code in codes:
        current_price = fetchCurrentStockPrice(code, day)
        if current_price:
            result.append(current_price)
    return jsonify(result)


def distinctAndSplit(codes):
    return list(set(codes.split(",")))


def fetchCurrentStockPrice(code, day):
    stock = fdr.DataReader(code, day)
    if stock.empty:
        return False
    df = stock[['Close']]
    return {
        "code": code,
        "price": str(df.iloc[-1][0])
    }


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
