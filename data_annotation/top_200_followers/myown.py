import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('top_200_youtubers.csv')

# Count the number of rows with null values in the 'Category' column
null_count = df['followers'].isnull().sum()
print(null_count)
# print(null_count)
# for i, val in df.iterrows():
#     if val[""]