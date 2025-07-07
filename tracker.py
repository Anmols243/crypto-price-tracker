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
    nargs="+",
    help="Coins to track (e.g. bitcoin, ethereum)"
)

parser.add_argument(
    "-cur", "--currency",
    default="usd",
    help="Currency to display price in (e.g. usd, eur, inr). Default is usd."
)

args = parser.parse_args()

coins = [c.lower() for c in args.coin]
id_parms = ",".join(coins)
currency = args.currency.lower()

url = "https://api.coingecko.com/api/v3/simple/price"
response = None
last_price = {}

try:
    while True:
        now = datetime.datetime.now().strftime("%I:%M:%S %p, %d %b %Y")

        try:
            params = {
                "ids": id_parms,
                "vs_currencies": currency
            }
            response = requests.get(url, params=params)

            if response.status_code == 429:
                print("Rate limit hit, waiting 60 seconds...")
                time.sleep(60)
                continue

            response.raise_for_status()
            data = response.json()
            
            for coin in coins:
                
                coin_data = data.get(coin)

                if coin_data is None:
                    print(Fore.RED + f"'{coin}' not found or is invalid.")
                    break

                if not coin_data: 
                    print(Fore.RED + f"'{currency}' not found or is invalid for '{coin}'.")
                    break

                price = coin_data.get(currency)
                
                if price is None:
                    print(Fore.RED + f"'{currency}' not found or is invalid for '{coin}'.")
                    break
                
                if last_price.get(coin) != price:
                    print(Fore.GREEN + f"\n[{now}] {coin.upper()}: {price} {currency.upper()}")
                    last_price[coin] = price
            
            time.sleep(15)
            
        except requests.exceptions.RequestException as e:
            short_error = str(e).split('\n')[0]
            print(Fore.RED + "Network/Api error:", Fore.YELLOW + short_error)
            print(Fore.CYAN + "Retrying in 10 seconds...\n")
            time.sleep(10)
            continue

except KeyboardInterrupt:
    print(Fore.RED + "Interrupted by the user.")
