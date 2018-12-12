import requests
from datetime import datetime




class CurrencyConverter:
    def __init__(self):
        currentRatio = self.getCurrentRatio()

        self.EUR_HNL = currentRatio
        self.HNL_EUR = currentRatio

    def getCurrentRatio(self):
        query = 'https://free.currencyconverterapi.com/api/v6/convert?q=EUR_HNL,HNL_EUR&compact=ultra'
        result = requests.get(query)

        status = result.status_code
        return result.json()

if __name__ == '__main__':
    cur = CurrencyConverter()
    print(cur.EUR_HNL)
