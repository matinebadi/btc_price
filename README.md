

# BTC Price Checker 🪙

**A simple Python script to fetch and display the current price of Bitcoin (BTC) using the CoinGecko API.**


## 🚀 Features
- Fetches **real-time Bitcoin price** in USD.
- Lightweight and easy to use.
- Simple, clean code structure.


## 📋 Requirements
Before running the script, make sure you have the following:
- Python 3.x installed
- The `requests` library

You can install the required library using pip:
```bash
pip install requests



🛠 Usage

1. Clone this repository:

git clone https://github.com/your_username/btc_price.git
cd btc_price


2. Run the script:

python btc_price.py


3. The current Bitcoin price will be displayed in your terminal:

current price:-> $27123.45



📜 Code Explanation

The script fetches Bitcoin's price from the CoinGecko API and displays it in USD. Here's a breakdown of the key parts:

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

API Used: CoinGecko API.

Handles errors gracefully by checking the response status code.




📸 Example Output

Here’s what you’ll see when the script runs successfully:

current price:-> $27123.45

If there’s an issue (e.g., no internet connection), you’ll see:

Error in price display.



🤝 Contributions

Contributions are welcome! Feel free to fork this repository and submit a pull request with your improvements or suggestions.



📝 License

This project is licensed under the MIT License.




🌟 Acknowledgments

Thanks to CoinGecko for providing the API to fetch Bitcoin prices.


