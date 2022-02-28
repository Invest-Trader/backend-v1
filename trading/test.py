
import requests
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=ADA&market=CNY&apikey=HMC1DK1A7OZTQJY0'
r = requests.get(url)
data = r.json()

print(data)