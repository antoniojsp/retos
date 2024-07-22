import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('paid-ads-top-campaigns-table_2023-11-30_2023-12-29.csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Convert `Created on` to datetime
df['Created on'] = pd.to_datetime(df['Created on'])

# Filter data for required campaign and creation date
filtered_data = df[(df['Campaign name'] == 'Campaign for OUTCOME_SALES') &
                   (df['Created on'] == '2023-08-16')]

# Get `Total sales` value
sales_value = filtered_data['Total sales'].values[0]

# Print the value of `Total sales` for the specified Campaign
print(f"`Total sales` for the campaign named 'Campaign for OUTCOME_SALES' created on 2023-08-16 is: {sales_value}")
