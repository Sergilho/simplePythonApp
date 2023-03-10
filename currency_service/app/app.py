from flask import Flask, jsonify
from currency_service.service.service import CurrenciesService

app = Flask(__name__)
service = CurrenciesService("https://economia.awesomeapi.com.br/all", 5)


@app.route('/currencies')
def Load():
    return service.Get()


@app.route('/currency/<code>')
def GetByCode(code):
    currency = service.GetByCode(code)
    if currency is None:
        return jsonify({"error": "Currency not found"}), 404
    return jsonify(currency)


if __name__ == '__main__':
    app.run()
