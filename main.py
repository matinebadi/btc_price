import requests

def btc__price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        btc_price = data['bitcoin']['usd']
        return btc_price
    else:
        return None

btc_price = btc__price()
if btc_price is not None:
    print(f'current price:-> ${btc_price}')
else:
    print('Error in price display.')
