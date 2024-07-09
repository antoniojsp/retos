import pandas as pd
import math
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('sales_memos.csv')

# # Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))
# Select rows where 'column_name' is equal to 'value1'
selected_rows = df[df['Company'] == 'EDAFLORS'].copy()

values = {}

for index, val in selected_rows.iterrows():
    if type(val["Date"]) == type("str"):
        month = val["Date"][3:]
        values[month] = values.get(month, 0) + float(val["Commission"][3:].replace('.', '').replace(',', '.'))
sorted_dict = dict(sorted(values.items()))
for i in sorted_dict.items():
    print(i)