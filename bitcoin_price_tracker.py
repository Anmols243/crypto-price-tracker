"""
Bitcoin Price Tracker CLI Tool
Fetches real-time Bitcoin price using CoinGecko API every 20 seconds.
Displays color-coded output with timestamp and handles errors gracefully.
"""

import requests
import datetime
import time
import colorama
from colorama import Fore
colorama.init(autoreset=True)


url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
response = None

try:
    while True:
        now = datetime.datetime.now().strftime("%I:%M:%S %p, %d %b %Y")

        try:
            response = requests.get(url)
            if response.status_code == 429:
                print("Rate limit hit, waiting 60 seconds...")
                time.sleep(60)
                continue
            
            response.raise_for_status()
            price = response.json()['bitcoin']['usd']
            print(Fore.GREEN + f"As of {now}, Price of bitcoin is ${price}.")
            time.sleep(20)
        
        except requests.exceptions.RequestException as e:

            short_error = str(e).split('\n')[0]
            print(Fore.RED  + "Network/Api error:", Fore.YELLOW + short_error)
            print(Fore.CYAN +"Retrying in 10 seconds...\n")
            time.sleep(10)
            continue
            
except KeyboardInterrupt:
    print(Fore.RED + "Interrupted by the user.")

        
            
    
        
        
        
