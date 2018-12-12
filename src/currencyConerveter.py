import requests
query = 'https://free.currencyconverterapi.com/api/v6/convert?q=EUR_HNL,HNL_EUR&compact=ultra'

result = requests.get(query)

print('Status:{}'.format(result.status_code))
print(result.json())
