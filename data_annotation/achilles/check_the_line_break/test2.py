import pandas as pd
import numpy as np


def check_line_break(df, p1, p2, column_name, last_price):
    """Determines if a price has broken a trend line formed by two pivot points."""

    # Calculate the slope and intercept of the trend line
    time_diff = (p2.index - p1.index).total_seconds()
    price_diff = p2[column_name] - p1[column_name]
    slope = price_diff / time_diff
    intercept = p1[column_name] - slope * p1.index[0].timestamp()

    # Function to calculate the trend line price at a given time
    def trend_line_price(timestamp):
        return slope * timestamp + intercept

    # Get the second to last row's timestamp and close price
    second_last_time = df.index[-2].timestamp()
    current_price = df['Close'].iloc[-2]

    # Calculate the trend line price at the second to last row
    line_price = trend_line_price(second_last_time)

    # Check if both the second to last price and the last price have crossed the trend line
    if column_name == 'Highs':
        is_broken = (df[column_name].iloc[-2] > trend_line_price(second_last_time) and
                     last_price[column_name] > trend_line_price(last_price.index[0].timestamp()))
    elif column_name == 'Lows':
        is_broken = (df[column_name].iloc[-2] < trend_line_price(second_last_time) and
                     last_price[column_name] < trend_line_price(last_price.index[0].timestamp()))
    else:
        raise ValueError("column_name must be either 'Highs' or 'Lows'")

    return {
        'is_broken': is_broken,
        'current_price': current_price,
        'line_price': line_price
    }

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

p1 = pd.Series({'Highs': 11}, index=pd.to_datetime(['2023-10-26 10:00:00']))
p2 = pd.Series({'Highs': 13}, index=pd.to_datetime(['2023-10-26 10:30:00']))
last_price = pd.Series({'Highs': 14}, index=pd.to_datetime(['2023-10-26 11:00:00']))

result = check_line_break(df, p1, p2, 'Highs', last_price)
print(result)