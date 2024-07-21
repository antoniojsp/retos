import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the TSV file into a DataFrame
df = pd.read_csv("meal_tracker.tsv", delimiter="\t")
summed_df = df.groupby('Date').sum().reset_index()
print(summed_df[summed_df["Calories"] == summed_df["Calories"].max()])