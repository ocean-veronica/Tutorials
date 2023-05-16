import pandas as pd

# Load the dataset from the CSV file
df = pd.read_csv('cryptocurrency_data.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Define the start and end dates for the desired period
start_date = '2020-01-01'
end_date = '2021-12-31'

# Filter the dataset based on the specified period and cryptocurrencies
filtered_df = df.loc[(df['Date'] >= start_date) & (df['Date'] <= end_date) & df['Symbol'].isin(['BTC', 'ETH'])]

# Group the data by symbol
grouped_df = filtered_df.groupby('Symbol')

# Calculate the annualized rate of return for each cryptocurrency
annualized_returns = {}
for symbol, data in grouped_df:
    initial_price = data.iloc[0]['Close']
    final_price = data.iloc[-1]['Close']
    num_years = (data.iloc[-1]['Date'] - data.iloc[0]['Date']).days / 365
    rate_of_return = (final_price / initial_price) ** (1 / num_years) - 1
    annualized_returns[symbol] = rate_of_return

# Sort the results in descending order of rate of return
sorted_returns = sorted(annualized_returns.items(), key=lambda x: x[1], reverse=True)

# Print the results
for symbol, rate_of_return in sorted_returns:
    print(f"{symbol}: {rate_of_return:.2%}")
