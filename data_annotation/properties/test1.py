import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame with latin-1 encoding
df_real_estate = pd.read_csv('Real Estate Mumbai Database - Rgdcvvvh.csv', encoding='latin-1')

# Display the first 5 rows
print(df_real_estate.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df_real_estate.info())
# Filter the data on `PROPERTY STREET`='172 Sir Bhalchandra Road' and `TRANSACTION DATE`='8/2/2023'
filtered_df = df_real_estate[(df_real_estate['PROPERTY STREET'] == '172 Sir Bhalchandra Road') & (df_real_estate['TRANSACTION DATE'] == '8/2/2023')]

# If there are more than 20 rows in the filtered dataset, display the first 20 rows
if (filtered_df.shape[0] > 20):
  print(filtered_df.head(20).to_markdown(index=False, numalign="left", stralign="left"))

# Otherwise, display all rows in the filtered dataset
else:
  print(filtered_df.to_markdown(index=False, numalign="left", stralign="left"))