import requests
from datetime import datetime
import json




class CurrencyConverter:
    def __init__(self):
        currentRatio, status = self.getCurrentRatio()
        #print(status)
        if status == 200:

            self.lastUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            currentRatio['lastUpdate'] = self.lastUpdate
            with open('DATA/currency.json', 'w') as f:
                json.dump(currentRatio, f)
        else:
            with open('DATA/currency.json') as f:
                currentRatio = json.load(f)

            self.lastUpdate = currentRatio['lastUpdate']

        self.EUR_HNL = currentRatio['EUR_HNL']
        self.HNL_EUR = currentRatio['HNL_EUR']



    def getCurrentRatio(self):
        query = 'https://free.currencyconverterapi.com/api/v6/convert?q=EUR_HNL,HNL_EUR&compact=ultra'
        result = requests.get(query)

        status = result.status_code
        return result.json(), status

    def eurToHnl(self, quantity):
        return quantity*self.EUR_HNL

    def hnlToEur(self, quantity):
        return quantity*self.HNL_EUR

if __name__ == '__main__':
    cur = CurrencyConverter()
    print(cur.hnlToEur(999))
    print(cur.eurToHnl(17))
    print(cur.lastUpdate)
