"""
Crypto Price Tracker CLI Tool
Fetches real-time Crypto price using CoinGecko API every 20 seconds.
Displays color-coded output with timestamp and handles errors gracefully.
"""
import argparse
import requests
import datetime
import time
import colorama
from colorama import Fore

colorama.init(autoreset=True)

parser = argparse.ArgumentParser(description="Track Crypto Prices")
parser.add_argument(
    "-c", "--coin",
    required=True,
    help="Coin to track (e.g. bitcoin, ethereum)"
)

parser.add_argument(
    "-cur", "--currency",
    default="usd",
    help="Currency to display price in (e.g. usd, eur, inr). Default is usd."
)

args = parser.parse_args()

coin = args.coin.lower()
currency = args.currency.lower()

url = "https://api.coingecko.com/api/v3/simple/price"
response = None

try:
    while True:
        now = datetime.datetime.now().strftime("%I:%M:%S %p, %d %b %Y")

        try:
            params = {
                "ids": coin,
                "vs_currencies": currency
            }
            response = requests.get(url, params=params)

            if response.status_code == 429:
                print("Rate limit hit, waiting 60 seconds...")
                time.sleep(60)
                continue

            response.raise_for_status()
            data = response.json()

            coin_data = data.get(coin)

            if coin_data is None:
                print(Fore.RED + f"Coin '{coin}' not found or is invalid.")
                break

            if not coin_data: 
                print(Fore.RED + f"Currency '{currency}' not found or is invalid for coin '{coin}'.")
                break

            price = coin_data.get(currency)
            if price is None:
                print(Fore.RED + f"Currency '{currency}' not found or is invalid for coin '{coin}'.")
                break
            
            print(Fore.GREEN + f"As of {now}, Price of {coin} is {currency.upper()} {price}.")
            time.sleep(30)
            
        except requests.exceptions.RequestException as e:
            short_error = str(e).split('\n')[0]
            print(Fore.RED + "Network/Api error:", Fore.YELLOW + short_error)
            print(Fore.CYAN + "Retrying in 10 seconds...\n")
            time.sleep(10)
            continue

except KeyboardInterrupt:
    print(Fore.RED + "Interrupted by the user.")
