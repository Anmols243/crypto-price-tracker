🪙 Real-time Crypto Price Tracker CLI
A Python CLI tool to track real-time prices of cryptocurrencies using the CoinGecko API. Supports multiple coins, live price updates every 15 seconds, and CSV logging for historical data.

🚀 Features
✅ Track multiple coins in real time (e.g., bitcoin, ethereum, dogecoin)

📈 Get live prices every 15 seconds (safe from API rate limits)

💾 Logs prices with timestamps to a local CSV file (price_log.csv)

⚠️ Smart handling of invalid coin names and user typos

🎨 Colored output using colorama for better readability

🛠️ Easy to run via command-line with simple arguments

🧰 Tech Stack
Python 3.10+

requests

argparse

colorama

csv

CoinGecko API (free, no auth required)

📦 Installation

git clone https://github.com/yourusername/crypto-price-tracker.git
cd crypto-price-tracker
pip install -r requirements.txt

🛠️ Usage
python tracker.py -c bitcoin ethereum dogecoin

| Flag                   | Description                       |
| ---------------------- | --------------------------------- |
| `-c` or `--coin`       | List of coins to track (required) |
| `-cur` or `--currency` | Fiat currency (default: `usd`)    |


📁 Sample CSV Output
timestamp,coin,price
2025-07-21 14:32:10,bitcoin,66230.34
2025-07-21 14:32:10,ethereum,3412.21

🧠 Learning Objectives
This project was built to strengthen:

API consumption with error handling

Real-world CLI tool development using argparse

Writing logs and data persistence using csv

Clean, maintainable scripting practices