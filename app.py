from flask import Flask, request, abort, jsonify, Response
import FinanceDataReader as fdr
from pykrx import stock
from datetime import date, timedelta
import logging

app = Flask(__name__)


# Health Check
@app.route('/ping')
def ping():
    return 'pong'


allowed_stock_type = ['KRX', 'NASDAQ', 'NYSE']


# 상장중인 종목 정보를 불러오는 API (국내 주식, 해외 주식)
@app.route('/api/v1/stock/code')
def getListedStockCodes():
    type = request.args.get('type')
    if type not in allowed_stock_type:
        abort(400, 'Bad Type')

    if type == 'KRX':
        return jsonify(getKrxCodes())

    df = fdr.StockListing(type)[['Symbol', 'Name']]
    return Response(df.to_json(orient='records'), mimetype='application/json')


def getKrxCodes():
    krx_stock_codes = []
    for ticker in stock.get_market_ticker_list(market='ALL'):
        name = stock.get_market_ticker_name(ticker)
        krx_stock_codes.append({
            "Symbol": ticker,
            "Name": name
        })
    return krx_stock_codes


# 해당하는 주식들의 현재가를 조회하는 API
@app.route('/api/v1/stock/price')
def getCurrentStockPrice():
    codes = request.args.get('codes')
    result = []
    last_day = date.today() - timedelta(days=14)
    for code in distinctAndSplit(codes):
        current_price = fetchCurrentStockPrice(code, last_day)
        if current_price:
            result.append(current_price)
    return jsonify(result)


def distinctAndSplit(codes):
    return list(set(codes.split(",")))


def fetchCurrentStockPrice(code, day):
    try:
        return {
            "code": code,
            "price": str(fdr.DataReader(code, day)[['Close']].iloc[-1][0])
        }
    except Exception as e:
        logging.error("주식 현재가를 불러오는 중 에러가 발생하였습니다 code: {0} error: {1}".format(code, e))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
