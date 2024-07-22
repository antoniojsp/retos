import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('Real Estate Mumbai Database - Rgdcvvvh.csv', encoding='latin-1')

# amount = df["AMOUNT IN (INR)"]
thousand = []
hundreth = []

for i, val in df.iterrows():

    tho = int(val["AMOUNT IN (INR)"]/1000)
    hun = val["AMOUNT IN (INR)"]%1000
    thousand.append(tho)
    hundreth.append(hun)

df["THOUSANDS"] = thousand
df["HUNDREDS"] = hundreth
print(df.to_string())