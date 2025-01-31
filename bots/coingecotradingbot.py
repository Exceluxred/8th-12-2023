import requests
import time

def get_price_data():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'ethereum',
        'vs_currencies': 'usd',
        'include_24hr_change': 'true'  # Include 24-hour price change in the response
    }

    # Make the GET request to the CoinGecko API
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if 'ethereum' in data and 'usd' in data['ethereum']:
            eth_price = data['ethereum']['usd']
            eth_price_change = data['ethereum']['usd_24h_change']
            return eth_price, eth_price_change
        else:
            print("Unexpected data format")
            return None, None
    else:
        print(f"Failed to fetch data, status code {response.status_code}")
        return None, None

def display_price_action():
    while True:
        # Get real-time price data
        eth_price, eth_price_change = get_price_data()

        if eth_price is not None:
            # Display the results
            print(f"Ethereum (ETH) Current Price: ${eth_price:.2f}")
            print(f"24h Price Change: {eth_price_change:.2f}%")
            print("-" * 40)
        else:
            print("Error fetching data. Retrying...")

        # Wait for a while before the next request (e.g., 10 seconds)
        time.sleep(10)

if __name__ == "__main__":
    display_price_action()
