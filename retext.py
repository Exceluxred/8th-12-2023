# import requests
# import time
# import pandas as pd
# import numpy as np
# import talib
# import logging
# from datetime import datetime, timedelta

# # Set up logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # Replace with your actual API key
# API_KEY = 'your_coinmarketcap_api_key'
# RISK_PERCENTAGE = 1  # Risk 1% of account balance per trade
# ACCOUNT_BALANCE = 10000  # Example account balance in USD

# def fetch_historical_data(symbol, interval='1h', limit=720):  # 720 hours = 1 month
#     url = f'https://min-api.cryptocompare.com/data/v2/histohour'
#     params = {
#         'fsym': symbol,
#         'tsym': 'USD',
#         'limit': limit,
#     }
#     try:
#         response = requests.get(url, params=params)
#         response.raise_for_status()
#         data = response.json()['Data']['Data']
#         df = pd.DataFrame(data)
#         df['time'] = pd.to_datetime(df['time'], unit='s')
#         df.set_index('time', inplace=True)
#         df.rename(columns={'close': 'Close', 'high': 'High', 'low': 'Low', 'open': 'Open', 'volumefrom': 'Volume'}, inplace=True)
#         return df
#     except requests.exceptions.RequestException as e:
#         logging.error(f"Failed to fetch historical data: {e}")
#         return None

# def calculate_technical_indicators(df):
#     df['SMA'] = talib.SMA(df['Close'], timeperiod=30)
#     df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
#     df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
#     return df

# def generate_trade_signal(df):
#     latest_row = df.iloc[-1]
#     signal = "Hold"
#     if latest_row['RSI'] < 30 and latest_row['MACD'] > latest_row['MACD_signal']:
#         signal = "Buy"
#     elif latest_row['RSI'] > 70 and latest_row['MACD'] < latest_row['MACD_signal']:
#         signal = "Sell"
#     return signal

# def calculate_position_size(entry_price, stop_loss_price, risk_percentage, account_balance):
#     risk_amount = account_balance * (risk_percentage / 100)
#     stop_loss_distance = abs(entry_price - stop_loss_price)
#     position_size = risk_amount / stop_loss_distance
#     return round(position_size, 2)

# def real_time_trade_loop(symbol):
#     while True:
#         logging.info(f"Fetching and analyzing data for {symbol}...")
#         df = fetch_historical_data(symbol)
#         if df is not None:
#             df = calculate_technical_indicators(df)
#             signal = generate_trade_signal(df)
#             latest_price = df['Close'].iloc[-1]

#             if signal == "Buy":
#                 stop_loss = latest_price * 0.98  # 2% below entry price
#                 take_profit = latest_price * 1.02  # 2% above entry price
#                 position_size = calculate_position_size(latest_price, stop_loss, RISK_PERCENTAGE, ACCOUNT_BALANCE)
#                 logging.info(f"BUY Signal: Price: {latest_price:.2f}, Stop-Loss: {stop_loss:.2f}, Take-Profit: {take_profit:.2f}, Position Size: {position_size}")

#             elif signal == "Sell":
#                 stop_loss = latest_price * 1.02  # 2% above entry price
#                 take_profit = latest_price * 0.98  # 2% below entry price
#                 position_size = calculate_position_size(latest_price, stop_loss, RISK_PERCENTAGE, ACCOUNT_BALANCE)
#                 logging.info(f"SELL Signal: Price: {latest_price:.2f}, Stop-Loss: {stop_loss:.2f}, Take-Profit: {take_profit:.2f}, Position Size: {position_size}")

#             else:
#                 logging.info(f"HOLD Signal: No action at price {latest_price:.2f}")

#         # Sleep for 1 hour before the next analysis
#         time.sleep(3600)

# if __name__ == "__main__":
#     symbol = 'BTC'  # Example: Bitcoin
#     real_time_trade_loop(symbol)

# import requests
# import time
# import pandas as pd
# import numpy as np
# import talib
# import logging
# from datetime import datetime, timedelta

# # Set up logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # Replace with your actual API key
# API_KEY = '5339a3d4-3c46-45e8-9c4e-0288c10ec36d'
# RISK_PERCENTAGE = 1  # Risk 1% of account balance per trade
# ACCOUNT_BALANCE = 10000  # Example account balance in USD

# def fetch_historical_data(symbol, interval='1h', limit=720):  # 720 hours = 1 month
#     url = f'https://min-api.cryptocompare.com/data/v2/histohour'
#     params = {
#         'fsym': symbol,
#         'tsym': 'USD',
#         'limit': limit,
#     }
#     try:
#         response = requests.get(url, params=params)
#         response.raise_for_status()
#         data = response.json()['Data']['Data']
#         df = pd.DataFrame(data)
#         df['time'] = pd.to_datetime(df['time'], unit='s')
#         df.set_index('time', inplace=True)
#         df.rename(columns={'close': 'Close', 'high': 'High', 'low': 'Low', 'open': 'Open', 'volumefrom': 'Volume'}, inplace=True)
#         return df
#     except requests.exceptions.RequestException as e:
#         logging.error(f"Failed to fetch historical data for {symbol}: {e}")
#         return None

# def calculate_technical_indicators(df):
#     df['SMA'] = talib.SMA(df['Close'], timeperiod=30)
#     df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
#     df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
#     return df

# def generate_trade_signal(df):
#     latest_row = df.iloc[-1]
#     signal = "Hold"
#     if latest_row['RSI'] < 30 and latest_row['MACD'] > latest_row['MACD_signal']:
#         signal = "Buy"
#     elif latest_row['RSI'] > 70 and latest_row['MACD'] < latest_row['MACD_signal']:
#         signal = "Sell"
#     return signal

# def calculate_position_size(entry_price, stop_loss_price, risk_percentage, account_balance):
#     risk_amount = account_balance * (risk_percentage / 100)
#     stop_loss_distance = abs(entry_price - stop_loss_price)
#     position_size = risk_amount / stop_loss_distance
#     return round(position_size, 2)

# def real_time_trade_loop(symbols):
#     while True:
#         for symbol in symbols:
#             logging.info(f"Fetching and analyzing data for {symbol}...")
#             df = fetch_historical_data(symbol)
#             if df is not None:
#                 df = calculate_technical_indicators(df)
#                 signal = generate_trade_signal(df)
#                 latest_price = df['Close'].iloc[-1]

#                 if signal == "Buy":
#                     stop_loss = latest_price * 0.98  # 2% below entry price
#                     take_profit = latest_price * 1.02  # 2% above entry price
#                     position_size = calculate_position_size(latest_price, stop_loss, RISK_PERCENTAGE, ACCOUNT_BALANCE)
#                     logging.info(f"{symbol} - BUY Signal: Price: {latest_price:.2f}, Stop-Loss: {stop_loss:.2f}, Take-Profit: {take_profit:.2f}, Position Size: {position_size}")

#                 elif signal == "Sell":
#                     stop_loss = latest_price * 1.02  # 2% above entry price
#                     take_profit = latest_price * 0.98  # 2% below entry price
#                     position_size = calculate_position_size(latest_price, stop_loss, RISK_PERCENTAGE, ACCOUNT_BALANCE)
#                     logging.info(f"{symbol} - SELL Signal: Price: {latest_price:.2f}, Stop-Loss: {stop_loss:.2f}, Take-Profit: {take_profit:.2f}, Position Size: {position_size}")

#                 else:
#                     logging.info(f"{symbol} - HOLD Signal: No action at price {latest_price:.2f}")

#         # Sleep for 1 hour before the next analysis
#         logging.info("Sleeping for 1 hour before the next analysis...")
#         time.sleep(3600)

# if __name__ == "__main__":
#     symbols = ['BTC', 'ETH', 'XRP', 'SOL']  # List of symbols to analyze
#     real_time_trade_loop(symbols)




import requests
import time
import pandas as pd
import numpy as np
import talib
import logging
from datetime import datetime, timedelta

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Replace with your actual API key
API_KEY = '5339a3d4-3c46-45e8-9c4e-0288c10ec36d'
RISK_PERCENTAGE = 1  # Risk 1% of account balance per trade
ACCOUNT_BALANCE = 10000  # Example account balance in USD

def fetch_historical_data(symbol, interval='1h', limit=720):  # 720 hours = 1 month
    """
    Fetch historical data for a given symbol and timeframe.
    """
    url = f'https://min-api.cryptocompare.com/data/v2/histohour'
    params = {
        'fsym': symbol,
        'tsym': 'USD',
        'limit': limit,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()['Data']['Data']
        df = pd.DataFrame(data)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.set_index('time', inplace=True)
        df.rename(columns={'close': 'Close', 'high': 'High', 'low': 'Low', 'open': 'Open', 'volumefrom': 'Volume'}, inplace=True)
        return df
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch historical data for {symbol}: {e}")
        return None

def calculate_technical_indicators(df):
    """
    Calculate technical indicators (RSI, MACD, SMA) for the DataFrame.
    """
    # Shorter RSI period for more sensitivity
    df['RSI'] = talib.RSI(df['Close'], timeperiod=10)
    # Adjusted MACD parameters for faster signals
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(df['Close'], fastperiod=8, slowperiod=17, signalperiod=9)
    # 50-period SMA for trend confirmation
    df['SMA'] = talib.SMA(df['Close'], timeperiod=50)
    return df

def generate_trade_signal(df):
    """
    Generate a trade signal based on RSI, MACD, and SMA.
    """
    latest_row = df.iloc[-1]
    signal = "Hold"

    # Log RSI and MACD values for debugging
    logging.info(f"RSI: {latest_row['RSI']}, MACD: {latest_row['MACD']}, MACD Signal: {latest_row['MACD_signal']}, SMA: {latest_row['SMA']}")

    # Buy signal: RSI oversold, MACD bullish crossover, and price above SMA
    if latest_row['RSI'] < 30 and latest_row['MACD'] > latest_row['MACD_signal'] and latest_row['Close'] > latest_row['SMA']:
        signal = "Buy"
    # Sell signal: RSI overbought, MACD bearish crossover, and price below SMA
    elif latest_row['RSI'] > 70 and latest_row['MACD'] < latest_row['MACD_signal'] and latest_row['Close'] < latest_row['SMA']:
        signal = "Sell"

    return signal

def calculate_position_size(entry_price, stop_loss_price, risk_percentage, account_balance):
    """
    Calculate the position size based on risk management rules.
    """
    risk_amount = account_balance * (risk_percentage / 100)
    stop_loss_distance = abs(entry_price - stop_loss_price)
    position_size = risk_amount / stop_loss_distance
    return round(position_size, 2)

def real_time_trade_loop(symbols, interval='1h', sleep_time=3600):
    """
    Main loop to fetch data, analyze, and generate trade signals.
    """
    while True:
        for symbol in symbols:
            logging.info(f"Fetching and analyzing data for {symbol}...")
            df = fetch_historical_data(symbol, interval=interval)
            if df is not None:
                df = calculate_technical_indicators(df)
                signal = generate_trade_signal(df)
                latest_price = df['Close'].iloc[-1]

                if signal == "Buy":
                    stop_loss = latest_price * 0.98  # 2% below entry price
                    take_profit = latest_price * 1.02  # 2% above entry price
                    position_size = calculate_position_size(latest_price, stop_loss, RISK_PERCENTAGE, ACCOUNT_BALANCE)
                    logging.info(f"{symbol} - BUY Signal: Price: {latest_price:.2f}, Stop-Loss: {stop_loss:.2f}, Take-Profit: {take_profit:.2f}, Position Size: {position_size}")

                elif signal == "Sell":
                    stop_loss = latest_price * 1.02  # 2% above entry price
                    take_profit = latest_price * 0.98  # 2% below entry price
                    position_size = calculate_position_size(latest_price, stop_loss, RISK_PERCENTAGE, ACCOUNT_BALANCE)
                    logging.info(f"{symbol} - SELL Signal: Price: {latest_price:.2f}, Stop-Loss: {stop_loss:.2f}, Take-Profit: {take_profit:.2f}, Position Size: {position_size}")

                else:
                    logging.info(f"{symbol} - HOLD Signal: No action at price {latest_price:.2f}")

        # Sleep before the next analysis
        logging.info(f"Sleeping for {sleep_time // 3600} hour(s) before the next analysis...")
        time.sleep(sleep_time)

if __name__ == "__main__":
    symbols = ['BTC', 'ETH', 'XRP', 'SOL']  # List of symbols to analyze
    real_time_trade_loop(symbols, interval='1h', sleep_time=3600)