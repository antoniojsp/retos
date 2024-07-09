import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the TSV file into a DataFrame
df = pd.read_csv('Retail Store Performance and Capacity Metrics - EXO2E Crypto - cccvvv.tsv', delimiter='\t')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Get all unique values from `Country`
unique_values = df['Country'].unique()

# Check the number of unique values in `Country`
if len(unique_values) > 50:
  # If there are too many unique values, sample the top 50
  top_occuring_values = df['Country'].value_counts().head(50).index.tolist()
  print(top_occuring_values)
else:
  # Otherwise print all unique valus in `Country`
  print(unique_values)


# # Create a new column called `Installed Capacity Difference`
# df['Installed Capacity Difference'] = df['Installed Capacity 30'] - df['Installed Capacity 20']
#
# # Insert the new column after the `Installed Capacity 30` column
# df.insert(df.columns.get_loc('Installed Capacity 30') + 1, 'Installed Capacity Difference', df.pop('Installed Capacity Difference'))
#
# # Reorder the columns
# df = df[['KeyMonth', 'calendar_date', 'Country', 'Key', 'Local', 'ownerships', 'GCS NGK',
#          'GCS Counter', 'GAP Capacity 20', 'GAP Capacity 30', 'Installed Capacity 20',
#          'Installed Capacity 30', 'Installed Capacity Difference', 'Category', 'Classification Number',
#          'Screen Cases', 'Classification', 'Screens', 'Counter Participation', 'NGK Participation',
#          'Annual Ranking', 'Performance', 'Total GCS', 'Type of Store', 'Special Day Hour Order',
#          'Daypart Hour Description', 'Ownerships Order', 'RankingMonth', 'Year', 'Quarter', 'Month', 'Day']]
#
# # Display the first 5 rows
# print(df.head().to_markdown(index=False, numalign="left", stralign="left"))
#
# # Print the column names and their data types
# print(df.info())

# Print column names
print(df.columns)
# Create a new column called `Installed Capacity Difference`
df['Installed Capacity Difference'] = df['Installed Capacity 30'] - df['Installed Capacity 20']

# Insert the new column after the `Installed Capacity 30` column
df.insert(df.columns.get_loc('Installed Capacity 30') + 1, 'Installed Capacity Difference', df.pop('Installed Capacity Difference'))

# Reorder the columns
df = df[['KeyMonth', 'calendar_date', 'Country', 'Key', 'Local', 'ownerships', 'GCS NGK',
         'GCS Counter ', 'GAP Capacity 20', 'GAP Capacity 30', 'Installed Capacity 20',
         'Installed Capacity 30', 'Installed Capacity Difference', 'Category', 'Classification Number',
         'Screen Cases', 'Classification', 'Screens', 'Counter Participation', 'NGK Participation',
         'Annual Ranking', 'Performance', 'Total GCS', 'Type of Store', 'Special Day Hour Order',
         'Daypart Hour Description', 'Ownerships Order', 'RankingMonth', 'Year', 'Quarter', 'Month', 'Day']]

# Print the first 5 rows of the dataframe
print(df.head().to_markdown(index=False, numalign="left", stralign="left")
)
# Print the column name and their data types
print(df.info())

# Write the dataframe to a csv file.
df.to_csv('retail_store_performance_installed_difference1.csv', index=False)
