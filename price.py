import requests
import datetime
import time

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

while True:
    now = datetime.datetime.now().strftime("%I:%M:%S %p, %d %b %Y")

    try:
        response = requests.get(url)
        response.raise_for_status()
        price = response.json()['bitcoin']['usd']
        print(f"As of {now}, Price of bitcoin is ${price}.")
        time.sleep(10)
            
    except KeyboardInterrupt:
        print("Interupted by the user")
        break
    
    except Exception as e:
        print("Error:", e)
        break
    
        
   
        
        
        
