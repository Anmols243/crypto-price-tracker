import requests
import datetime
import time
import colorama
from colorama import Fore
colorama.init(autoreset=True)


url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
try:
    while True:
        now = datetime.datetime.now().strftime("%I:%M:%S %p, %d %b %Y")

        try:
            response = requests.get(url)
            response.raise_for_status()
            price = response.json()['bitcoin']['usd']
            print(Fore.GREEN + f"As of {now}, Price of bitcoin is ${price}.")
            time.sleep(10)
        
        except requests.exceptions.RequestException as e:
            short_error = str(e).split('\n')[0]
            print(Fore.RED  + "Network/Api error:", Fore.YELLOW + short_error)
            print(Fore.CYAN +"Retrying in 10 seconds...\n")
            time.sleep()
            continue
        
except KeyboardInterrupt:
    print(Fore.RED + "Interrupted by the user.")

        
            
    
        
        
        
