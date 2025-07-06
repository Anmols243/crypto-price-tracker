"""
Bitcoin Price Tracker CLI Tool
Fetches real-time Bitcoin price using CoinGecko API every 20 seconds.
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
    "-c","--coin",
    nargs="+",
    default=["bitcoin"],
    help= "coins to track"
)
args = parser.parse_args()
coin = args.coin[0].lower()


url = "https://api.coingecko.com/api/v3/simple/price"
response = None

try:
    while True:
        now = datetime.datetime.now().strftime("%I:%M:%S %p, %d %b %Y")

        try:
            params ={
                "ids": coin,
                "vs_currencies": "usd"
            }
            response = requests.get(url, params=params)
            
            if response.status_code == 429:
                print("Rate limit hit, waiting 60 seconds...")
                time.sleep(60)
                continue
            
            response.raise_for_status()
            data = response.json()
            
            price = data.get(coin, {}).get("usd")
            if price:
                print(Fore.GREEN + f"As of {now}, Price of {coin} is ${price}.")
            else:
                print(Fore.RED + f"{coin.upper()} not found or is invalid")
            
            time.sleep(20)
        
        except requests.exceptions.RequestException as e:

            short_error = str(e).split('\n')[0]
            print(Fore.RED  + "Network/Api error:", Fore.YELLOW + short_error)
            print(Fore.CYAN +"Retrying in 10 seconds...\n")
            time.sleep(10)
            continue
            
except KeyboardInterrupt:
    print(Fore.RED + "Interrupted by the user.")
    

        
            
    
        
        
        
