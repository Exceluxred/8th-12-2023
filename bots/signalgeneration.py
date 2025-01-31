import pandas as pd
import schedule
import time
from oandapyV20 import API
from oandapyV20.endpoints import orders, instruments
import logging
import datetime

# Configuration
API_KEY = "your_api_key"
ACCOUNT_ID = "your_account_id"
INSTRUMENT = "EUR_USD"
TIMEFRAME = "M15"

# Initialize OANDA API Client once
client = API(access_token=API_KEY)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Signal Generator Function
def signal_generator(df):
    if len(df) < 2:
        return 0
    prev_open = df['Open'].iloc[-2]
    prev_close = df['Close'].iloc[-2]
    curr_open = df['Open'].iloc[-1]
    curr_close = df['Close'].iloc[-1]

    # Bearish Engulfing
    if prev_open < prev_close and curr_open > curr_close and curr_close < prev_open:
        return 1  # Sell Signal
    # Bullish Engulfing
    elif prev_open > prev_close and curr_open < curr_close and curr_close > prev_open:
        return 2  # Buy Signal
    else:
        return 0  # No Signal

# Get Live Candles from Broker
def get_candles(n=3):
    try:
        params = {"count": n, "granularity": TIMEFRAME}
        candles = instruments.InstrumentsCandles(instrument=INSTRUMENT, params=params)
        client.request(candles)
        return candles.response['candles']
    except Exception as e:
        logging.error(f"Error getting candles: {e}")
        return []

# Trading Job
def trading_job():
    candles = get_candles()
    if not candles:
        logging.warning("No candles received, skipping trade.")
        return
    
    # Format the data from candles
    data = {
        "Open": [float(c['mid']['o']) for c in candles],
        "High": [float(c['mid']['h']) for c in candles],
        "Low": [float(c['mid']['l']) for c in candles],
        "Close": [float(c['mid']['c']) for c in candles]
    }

    df = pd.DataFrame(data)
    logging.info(f"Dataframe: \n{df.tail()}")  # Show the most recent data

    # Generate trade signal
    signal = signal_generator(df)

    if signal != 0:
        prev_range = abs(df['Open'].iloc[-2] - df['Close'].iloc[-2])
        stop_loss = prev_range
        take_profit = 2 * stop_loss

        if signal == 1:  # Sell Signal
            stop_loss_price = df['Close'].iloc[-1] + stop_loss
            take_profit_price = df['Close'].iloc[-1] - take_profit
            order_data = {
                "order": {
                    "units": "-1000",
                    "instrument": INSTRUMENT,
                    "type": "MARKET",
                    "stopLossOnFill": {"price": str(stop_loss_price)},
                    "takeProfitOnFill": {"price": str(take_profit_price)}
                }
            }
        elif signal == 2:  # Buy Signal
            stop_loss_price = df['Close'].iloc[-1] - stop_loss
            take_profit_price = df['Close'].iloc[-1] + take_profit
            order_data = {
                "order": {
                    "units": "1000",
                    "instrument": INSTRUMENT,
                    "type": "MARKET",
                    "stopLossOnFill": {"price": str(stop_loss_price)},
                    "takeProfitOnFill": {"price": str(take_profit_price)}
                }
            }

        # Place the order
        try:
            order = orders.OrderCreate(ACCOUNT_ID, data=order_data)
            client.request(order)
            logging.info(f"Order Executed: {order.response}")
        except Exception as e:
            logging.error(f"Error executing order: {e}")

# Schedule the Trading Job
schedule.every(15).minutes.do(trading_job)

# Set a time limit for the script to run (e.g., 10 minutes for testing)
end_time = datetime.datetime.now() + datetime.timedelta(minutes=10)

# Run the Scheduler with Graceful Shutdown on KeyboardInterrupt
try:
    while datetime.datetime.now() < end_time:  # Runs for 10 minutes
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    logging.info("Script interrupted. Exiting gracefully.")
