from pybit.unified_trading import HTTP

# Install the pybit library
# pip install pybit


# Replace these with your API key and secret
api_key = "G2W4jhMBllVzwheiMI"
api_secret = "VXW9wECqFc6FkOsl2Ae0292gqIyjcDGYnJAR"

# Set up a connection to Bybit's API
session = HTTP(
    api_key=api_key,
    api_secret=api_secret,
    testnet=True  # Use True for testnet, False for live trading
)

# Example API call: Fetch wallet balance
try:
    balance = session.get_wallet_balance()
    print("Wallet Balance:", balance)
except Exception as e:
    print("Error:", e) 