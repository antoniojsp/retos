import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('top_200_youtubers.csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())
# Filter the data on `Country` column for 'US'
us_youtubers = df[df['Country'] == 'US']

# Write the dataframe to a tsv file
us_youtubers[['Channel Name', 'Country']].to_csv('us_youtubers.tsv', sep='\t', index=False)