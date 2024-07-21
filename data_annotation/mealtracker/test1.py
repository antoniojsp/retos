import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the TSV file into a DataFrame
df = pd.read_csv("meal_tracker.tsv", delimiter="\t")

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Group by `Date` and sum up the `Calories` for each date
calories_by_date = df.groupby('Date')['Calories'].sum()

# Sort in descending order of calories consumed
sorted_calories_by_date = calories_by_date.sort_values(ascending=False)

# Print the top 3 days with highest calories consumed
print(sorted_calories_by_date.head(3).to_markdown(numalign="left", stralign="left"))
