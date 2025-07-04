import requests
import json
import datetime

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

today = datetime.date.today()
now = datetime.datetime.now()
now = now.strftime("%I:%M %p, %d %b %Y")

try:
    response = requests.get(url)
    response.raise_for_status
    price = response.json()['bitcoin']['usd']
 
    
except Exception as e:
    print(e)
    
else:
    print(f"As of {now}, Price of bitcoin is ${price}.")
        
