import requests
import time

def get_price_data():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    
    # Parameters for the API request
    params = {
        'start': '1',           # Start from the top coin (e.g., Bitcoin)
        'limit': '50',          # Fetch top 50 coins (we'll filter later)
        'convert': 'USD',       # Convert the price into USD
    }

    # Set up headers with your API key
    headers = {
        'X-CMC_PRO_API_KEY': '5339a3d4-3c46-45e8-9c4e-0288c10ec36d',  # Replace with your actual API key
        'Accept': 'application/json',
    }

    # Make the GET request to the CoinMarketCap API
    response = requests.get(url, params=params, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            # Filter for Bitcoin (BTC), XRP (XRP), and Solana (SOL)
            coins_to_display = ['Bitcoin', 'XRP', 'Solana']
            for coin in data['data']:
                name = coin['name']
                if name in coins_to_display:
                    symbol = coin['symbol']
                    price = coin['quote']['USD']['price']
                    percent_change_24h = coin['quote']['USD']['percent_change_24h']
                    print(f"{name} ({symbol}): ${price:.2f}")
                    print(f"24h Price Change: {percent_change_24h:.2f}%")
                    print("-" * 40)
        else:
            print("Unexpected data format")
    else:
        print(f"Failed to fetch data, status code {response.status_code}")

def display_price_action():
    while True:
        get_price_data()

        # Sleep time before the next request (e.g., 30 seconds to avoid hitting the rate limit)
        time.sleep(30)

if __name__ == "__main__":
    display_price_action()



