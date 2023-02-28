from datetime import datetime, timedelta
import requests
from flask import Flask, jsonify

from currency_service.entities.entities import Currency


class CurrenciesService:
    _currencies = {}
    _url = "https://economia.awesomeapi.com.br/all"
    _timeToExpire: int = 5
    LastUpdate = None

    def __init__(self, url, timeToExpire):
        self._url = url
        self._timeToExpire = timeToExpire

    def Load(self):
        r = requests.get(self._url)
        data = r.json()
        for code in data:
            value = data[code]
            self._currencies[code.upper()] = Currency(code, value["name"], value["high"], value["low"],
                                                      value["varBid"], value["bid"], value["ask"])

        self.LastUpdate = datetime.now()

    def Get(self):
        if self.LastUpdate is None:
            self.Load()

        if datetime.now() - self.LastUpdate > timedelta(minutes=self._timeToExpire):
            self.Load()

        return jsonify(self._currencies)

    def GetByCode(self, code: str):
        if self.LastUpdate is None:
            self.Load()

        if datetime.now() - self.LastUpdate > timedelta(minutes=self._timeToExpire):
            self.Load()

        if code.upper() in self._currencies:
            return self._currencies[code.upper()]

        return None


app = Flask(__name__)
app.config["URL"] = "https://economia.awesomeapi.com.br/all"
app.config["TIME_TO_EXPIRE"] = 5
service = CurrenciesService(url=app.config.get("URL"), timeToExpire=app.config.get("TIME_TO_EXPIRE"))


@app.route('/currencies', methods=['GET'])
def get_all_currencies():
    return service.Get()


@app.route('/currency/<code>', methods=['GET'])
def get_currency_by_code(code):
    currency = service.GetByCode(code)
    if currency is None:
        return f"Currency {code} not found", 404
    return jsonify(currency.to_dict())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
