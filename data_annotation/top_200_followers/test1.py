import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('top_200_youtubers.csv')

# Count the number of rows with null values in the 'Category' column
null_count = df['Category'].isnull().sum()

print(null_count)

# Filter all rows of the dataframe which have null values in `followers` column
null_followers_df = df[df['followers'].isnull()]

# print the number of rows which have null values in `followers` column
print(f"Number of rows with null values in followers column:{null_followers_df.shape[0]}")
