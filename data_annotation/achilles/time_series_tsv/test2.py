import pandas as pd
import matplotlib.pyplot as plt

# Read the TSV file into a DataFrame
df_time_series = pd.read_csv('time_series.tsv', sep='\t')

# Convert the `Date` column to datetime format
df_time_series['Date'] = pd.to_datetime(df_time_series['Date'])

# Calculate the 7-day moving average of `Amount Untaxed`
df_time_series['Moving Average'] = df_time_series['Amount Untaxed'].rolling(window=7, min_periods=1).mean()

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(12, 6))

# Create a bar plot of `Amount Untaxed` by `Date`
ax.bar(df_time_series['Date'], df_time_series['Amount Untaxed'], color='skyblue', label='Amount Untaxed')

# Create a line plot of `Moving Average` by `Date`
ax.plot(df_time_series['Date'], df_time_series['Moving Average'], color='orange', label='7-Day Moving Average')

# Add labels and a title
ax.set_xlabel('Date')
ax.set_ylabel('Amount')
ax.set_title('Daily Amount Untaxed with 7-Day Moving Average')
ax.legend()

# Rotate the x-axis labels by 45 degrees
plt.xticks(rotation=45, ha='right')

# Display the plot
plt.show()