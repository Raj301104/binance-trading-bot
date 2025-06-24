import logging
from binance.client import Client
from binance.enums import *
import sys

# === Configure Logging ===
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        logging.info("Bot initialized with Testnet: %s", testnet)

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info("Market order placed: %s", order)
            print(f"Market order placed: {order}")
        except Exception as e:
            logging.error("Error placing market order: %s", e)
            print(f"Error placing market order: {e}")

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            logging.info("Limit order placed: %s", order)
            print(f"Limit order placed: {order}")
        except Exception as e:
            logging.error("Error placing limit order: %s", e)
            print(f"Error placing limit order: {e}")

def main():
    api_key = input("Enter your API Key: ")
    api_secret = input("Enter your API Secret: ")

    bot = BasicBot(api_key, api_secret)

    while True:
        print("\n=== Trading Bot ===")
        print("1. Place Market Order")
        print("2. Place Limit Order")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
            side = input("Enter side (BUY/SELL): ").upper()
            quantity = float(input("Enter quantity: "))
            bot.place_market_order(symbol, side, quantity)

        elif choice == '2':
            symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
            side = input("Enter side (BUY/SELL): ").upper()
            quantity = float(input("Enter quantity: "))
            price = float(input("Enter price: "))
            bot.place_limit_order(symbol, side, quantity, price)

        elif choice == '3':
            print("Exiting.")
            sys.exit()

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
