import csv
from datetime import datetime

# Define the start and end dates for the desired period
start_date = '2020-01-01'
end_date = '2021-12-31'

# Open the CSV file
with open('cryptocurrency_data.csv', 'r') as file:
    # Read the CSV file
    csv_reader = csv.DictReader(file)

    # Initialize dictionaries to store the data
    prices = {}
    dates = {}

    # Process each row in the CSV file
    for row in csv_reader:
        # Extract the symbol, date, and close price
        symbol = row['Symbol']
        date = datetime.strptime(row['Date'], '%Y-%m-%d').date()
        close_price = float(row['Close'])

        # Check if the date is within the desired period and for BTC or ETH
        if start_date <= row['Date'] <= end_date and symbol in ['BTC', 'ETH']:
            if symbol not in prices:
                prices[symbol] = []
                dates[symbol] = []
            prices[symbol].append(close_price)
            dates[symbol].append(date)

# Calculate the annualized rate of return for each cryptocurrency
annualized_returns = {}
for symbol in prices:
    initial_price = prices[symbol][0]
    final_price = prices[symbol][-1]
    num_years = (dates[symbol][-1] - dates[symbol][0]).days / 365
    rate_of_return = (final_price / initial_price) ** (1 / num_years) - 1
    annualized_returns[symbol] = rate_of_return

# Sort the results in descending order of rate of return
sorted_returns = sorted(annualized_returns.items(), key=lambda x: x[1], reverse=True)

# Print the results
for symbol, rate_of_return in sorted_returns:
    print(f"{symbol}: {rate_of_return:.2%}")
