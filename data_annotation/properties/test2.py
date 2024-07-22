import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Attempt to read the file again with 'ISO-8859-1' encoding to address the encoding issue
real_estate_df = pd.read_csv('Real Estate Mumbai Database - Rgdcvvvh.csv', encoding='ISO-8859-1')

# Display the columns of the real estate dataframe again
print(real_estate_df.columns)