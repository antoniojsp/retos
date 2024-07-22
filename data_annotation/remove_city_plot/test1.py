import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV files into DataFrames
df_ny = pd.read_csv('population_ny.csv')
df_ma = pd.read_csv('population_ma.csv')

# Display the first 5 rows of each DataFrame
print("Population in NY:\n")
print(df_ny.head())
print("\nPopulation in MA:\n")
print(df_ma.head())

# Print the column names and their data types
print("\nColumn names and data types in NY population dataset:\n")
print(df_ny.info())
print("\nColumn names and data types in MA population dataset:\n")
print(df_ma.info())

# Remove the ',' in the `Population` column and convert the column to numeric
df_ny['Population'] = pd.to_numeric(df_ny['Population'].str.replace(',', ''))
df_ma['Population'] = pd.to_numeric(df_ma['Population'].str.replace(',', ''))

# Filter the DataFrames and save the results to new CSV files
df_ny[df_ny['Population'] >= 100_000].to_csv('population_ny_filtered.csv', index=False)
df_ma[df_ma['Population'] >= 100_000].to_csv('population_ma_filtered.csv', index=False)

import altair as alt

# Create the chart, sorting by population in descending order
chart = alt.Chart(df_ma_raw).mark_bar().encode(
    x=alt.X('City', sort='-y'),
    y=alt.Y('Population'),
    tooltip=['City', 'Population']
).properties(
    title='City Populations in MA'
).interactive()

# Save the chart
chart.save('city_populations_in_ma_bar_chart.json')
