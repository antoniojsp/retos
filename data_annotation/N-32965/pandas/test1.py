import pandas as pd

# Read the CSV file
df = pd.read_csv('data.csv')

# Print the first few rows of the DataFrame
print(df.info())


df["profit"] = df["revenue"] - df["cost"]

chan = df.groupby("channel")["profit"].sum()
chan1 = df.groupby("channel")["profit"].mean()


print("Average")
print(chan1)
print("Total")
print(chan.to_string())

