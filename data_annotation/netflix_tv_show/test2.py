import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
netflix_data = pd.read_csv('Netflix_TV_Shows_and_Movies.csv')

# Display the first 5 rows
print(netflix_data.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(netflix_data.info())

# Filter data for movies and shows produced in the US with an IMDB score of 6.0 or higher
filtered_data = netflix_data[
    (netflix_data['production_countries'].str.contains('US')) &
    (netflix_data['imdb_score'] >= 6.0)
]

# Calculate the total runtime
total_runtime = filtered_data['runtime'].sum()


print(total_runtime)