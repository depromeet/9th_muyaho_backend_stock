from flask import Flask, request, abort, jsonify, Response
import FinanceDataReader as fdr
from pykrx import stock
from datetime import date, timedelta

app = Flask(__name__)


@app.route('/ping')
def hello_world():
    return 'OK'


@app.route('/api/v1/stock/code')
def getDomesticCode():
    type = request.args.get('type')
    if type not in ['KRX', 'NASDAQ']:
        abort(400, 'Bad Type')
    if type == 'KRX':
        return jsonify(getKRXCodes())
    df = fdr.StockListing('NASDAQ')[['Symbol', 'Name']]
    return Response(df.to_json(orient='records'), mimetype='application/json')


def getKRXCodes():
    result = []
    for ticker in stock.get_market_ticker_list(market='ALL'):
        name = stock.get_market_ticker_name(ticker)
        result.append({
            "Symbol": ticker,
            "Name": name
        })
    return result


@app.route('/api/v1/stock/price')
def getPrice():
    codes = request.args.get('codes').split(",")
    result = []

    for code in codes:
        today = date.today()
        day = today - timedelta(days=14)
        if fdr.DataReader(code, day).empty:
            abort(404, 'Not Found Stock')
        df = fdr.DataReader(code, day)[['Close']]
        result.append({
            "code": code,
            "price": str(df.iloc[-1][0])
        })
    return jsonify(result)


if __name__ == '__main__':
    app.run()
