import yfinance as yf
import pandas as pd
import time
import vectorbt as vbt

# List of 20 US stocks and ETFs
tickers = [
    'AAPL',
    'MSFT',
    'GOOGL',
    'AMZN',
    'META',
    'TSLA',
    'NVDA',
]

# Initialize an empty dictionary to store data for each ticker
data_dict = {}

# Download data for each ticker sequentially
for ticker in tickers:
    try:
        # Download data for the current ticker
        data = yf.download(ticker, start="2024-01-01", end="2025-01-01", auto_adjust=False)
        
        # Store the data in the dictionary
        data_dict[ticker] = data
        
        # Add a small delay (e.g., 1 second) to avoid rate limiting
        time.sleep(1)
    
    except Exception as e:
        print(f"Failed to download data for {ticker}: {e}")

# Combine all data into a single DataFrame
data = pd.concat(data_dict, axis=1)

# Display the first few rows of the combined data
print(data.head())

# Display the first few rows of the combined data



