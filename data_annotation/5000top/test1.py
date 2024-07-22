import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV files into Pandas Dataframes
df_south_america = pd.read_csv('s_america.csv')
df_asia = pd.read_csv('asia.csv')
df_europe = pd.read_csv('europe.csv')

# Display the first 5 rows of each DataFrame
print("First 5 rows of South America DataFrame:")
print(df_south_america.head().to_markdown(index=False, numalign="left", stralign="left"))

print("\nFirst 5 rows of Asia DataFrame:")
print(df_asia.head().to_markdown(index=False, numalign="left", stralign="left"))

print("\nFirst 5 rows of Europe DataFrame:")
print(df_europe.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types for each DataFrame
print("\nColumn names and their data types for South America DataFrame:")
print(df_south_america.info())

print("\nColumn names and their data types for Asia DataFrame:")
print(df_asia.info())

print("\nColumn names and their data types for Europe DataFrame:")
print(df_europe.info())

# Rename the `Average Age (Years)` column in `df_asia` and `df_europe` to `Average Age`
df_asia = df_asia.rename(columns={'Average Age (Years)': 'Average Age'})
df_europe = df_europe.rename(columns={'Average Age (Years)': 'Average Age'})

# Rename `Population (Approx.)` column in `df_asia` to `Population`
df_asia = df_asia.rename(columns={'Population (Approx.)': 'Population'})

# Multiply the `Population (Million)` column in `df_europe` by 1000000 and rename it to `Population`
df_europe = df_europe.rename(columns={'Population (Million)': 'Population'})
df_europe['Population'] = df_europe['Population'] * 1000000

# Concatenate the three DataFrames `df_south_america`, `df_asia`, and `df_europe` into a single DataFrame `df_combined`
df_combined = pd.concat([df_south_america, df_asia, df_europe], ignore_index=True)

# Calculate the mean of `Population` and `Average Age` columns in `df_combined` and print the results
average_population = df_combined['Population'].mean()
average_age = df_combined['Average Age'].mean()

print(f"Average Population across all countries: {average_population:.2f}")
print(f"Average Age across all countries: {average_age:.2f}")