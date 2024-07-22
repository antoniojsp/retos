import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('top_200_youtubers.csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Now that we have the structure, let's filter out only the US YouTubers and save it to a TSV file.
us_youtubers = df[df['Country'] == 'US']

# Saving to a TSV file
output_file_path = 'usa_youtubers.tsv'
us_youtubers.to_csv(output_file_path, sep='\t', index=False)

print(output_file_path)