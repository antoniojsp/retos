def check_line_break(df, p1, p2, column_name, last_price):
    """Determines if a price has broken a trend line formed by two pivot points.

    Args:
      df: A Pandas DataFrame containing OHLCV data with a datetime index.
          This DataFrame should also contain a column named 'HISTOGRAM'
          representing the MACD histogram values.
      p1: A Pandas Series representing the first pivot point, containing
          'Highs' or 'Lows' value and a datetime index.
      p2: A Pandas Series representing the second pivot point, containing
          'Highs' or 'Lows' value and a datetime index.
      column_name: A string, either 'Highs' or 'Lows', indicating which price
          column to use for the line break check.
      last_price: A Pandas Series representing the latest price, containing
          'Highs' or 'Lows' value and a datetime index.

    Returns:
      A dictionary with the following keys:
        is_broken: A boolean value indicating whether the line is broken.
        current_price: The 'Close' price from the second to last row in the DataFrame.
        line_price: The calculated price of the trend line at the time of the
                    second to last row in the DataFrame.
    """
    # Calculate slope and intercept of the trend line
    slope = (p2[column_name] - p1[column_name]) / (p2.index[0] - p1.index[0]).total_seconds()
    intercept = p1[column_name] - slope * p1.index[0].timestamp()

    # Calculate the price of the trend line at the time of the second to last row in the DataFrame
    line_price = slope * df.index[-2].timestamp() + intercept

    # Get the 'Close' price from the second to last row in the DataFrame
    current_price = df['Close'].iloc[-2]

    # Check if the line is broken
    if column_name == 'Highs':
        is_broken = current_price > line_price and last_price[column_name] > line_price
    elif column_name == 'Lows':
        is_broken = current_price < line_price and last_price[column_name] < line_price
    else:
        raise ValueError("Invalid column name. Choose 'Highs' or 'Lows'.")

    return {'is_broken': is_broken, 'current_price': current_price, 'line_price': line_price}


import pandas as pd

# Sample data
data = {
    'Open': [10, 11, 12, 13, 14],
    'Highs': [11, 12, 13, 14, 15],
    'Low': [9, 10, 11, 12, 13],
    'Close': [10.5, 11.5, 12.5, 13.5, 14.5],
    'Volume': [100, 110, 120, 130, 140],
    'HISTOGRAM': [0.1, 0.2, -0.1, -0.2, 0.1]
}
df = pd.DataFrame(data, index=pd.to_datetime(['2023-10-26 10:00:00', '2023-10-26 10:15:00', '2023-10-26 10:30:00', '2023-10-26 10:45:00', '2023-10-26 11:00:00']))
print(df.to_string())
p1 = pd.Series({'Highs': 11}, index=pd.to_datetime(['2023-10-26 10:00:00']))
p2 = pd.Series({'Highs': 13}, index=pd.to_datetime(['2023-10-26 10:30:00']))
last_price = pd.Series({'Highs': 14}, index=pd.to_datetime(['2023-10-26 11:00:00']))

result = check_line_break(df, p1, p2, 'Highs', last_price)
print(result)