import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('Netflix_TV_Shows_and_Movies.csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

import ast

# Convert the `production_countries` column to a list of countries
df['production_countries'] = df['production_countries'].astype(str).apply(lambda x: ast.literal_eval(x))

# Filter the data based on the given conditions
filtered_df = df[
    (df['production_countries'].apply(lambda x: 'US' in x)) &
    (df['imdb_score'] >= 6.0) &
    (df['type'].isin(['SHOW', 'MOVIE']))
    ]

# Calculate the total runtime and print the result
total_runtime = filtered_df['runtime'].sum()
print(f"The total runtime of all US-produced movies and shows with an IMDB score of 6.0 or higher is: {total_runtime}")
