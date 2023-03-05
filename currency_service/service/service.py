from datetime import datetime, timedelta
import requests
from flask import jsonify

from currency_service.entities.entities import Currency


class CurrenciesService:
    _currencies = {}
    _url = ""
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
