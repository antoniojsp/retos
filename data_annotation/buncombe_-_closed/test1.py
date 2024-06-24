import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv("Buncombe_-_Closed_SFR_-_11_30_23_-_12_30_23_-_Sheet1(1).csv", skiprows=1)

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Print descriptive statistics of `Days on Market to Close`
print("Descriptive statistics of Days on Market to Close:\n")
print(df['Days on Market to Close'].describe().to_markdown(numalign="left", stralign="left"))

# Calculate and print the mean of `Days on Market to Close`
avg_days_on_market = df['Days on Market to Close'].mean()

# Round the result to 2 decimal places
avg_days_on_market_rounded = round(avg_days_on_market, 2)

print(f"\nAverage Days on Market to Close: {avg_days_on_market_rounded}")
