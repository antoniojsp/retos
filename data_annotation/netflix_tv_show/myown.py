import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('Netflix_TV_Shows_and_Movies.csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
df_filter = df[df["imdb_score"] >= 6]
runtime = 0

for i, val in df_filter.iterrows():
    if 'US' in val["production_countries"]:
        runtime+=val["runtime"]

print(f"Total runtime of all movies and series produce in the US with a score 6 or higher is { runtime }")