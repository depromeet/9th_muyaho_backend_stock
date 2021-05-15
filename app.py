from flask import Flask, request, abort, jsonify
import FinanceDataReader as fdr
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

    df = fdr.StockListing(type)[['Symbol', 'Name']]
    return df.to_json(orient='records')


@app.route('/api/v1/stock/price')
def getPrice():
    codes = request.args.get('codes').split(",")
    result = []

    for code in codes:
        today = date.today()
        week = today.weekday()
        if week >= 5:
            today -= timedelta(days=week - 4)
        df = fdr.DataReader(code, today)[['Close']]

        result.append({
            "code": code,
            "price": str(df.values[0][0])
        })
    return jsonify(result)


if __name__ == '__main__':
    app.run()
