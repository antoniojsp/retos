import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame with latin-1 encoding
df = pd.read_csv('Real Estate Mumbai Database - Rgdcvvvh.csv', encoding='latin-1')


result = df[df['PROPERTY STREET'] == '172 Sir Bhalchandra Road']
result = result[result["TRANSACTION DATE"] == "8/2/2023"]
print(result)