import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the TSV file into a DataFrame
df = pd.read_csv('meal_tracker.tsv', delimiter='\t')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Aggregate calories by date
df_agg = df.groupby('Date')['Calories'].sum().reset_index(name='Total_Calories')

# Sort by total calories in descending order
df_agg_sorted = df_agg.sort_values(by='Total_Calories', ascending=False)

# Get the date with the highest calorie intake
highest_calorie_date = df_agg_sorted.iloc[0]['Date']
highest_calories = df_agg_sorted.iloc[0]['Total_Calories']

# Print the result
print(f"The date with the highest calorie intake was {highest_calorie_date} with {highest_calories} calories.")
