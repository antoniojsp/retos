import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('uk_universities.csv')

# Display the first 5 rows
print(df.head())

# Print the column names and their data types
print(df.info())

from pandas.api.types import is_numeric_dtype

for column_name in ['Minimum_IELTS_score']:
  if not is_numeric_dtype(df[column_name]):
    # Assume CSV columns can only be numeric or string.
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')

df.drop_duplicates(subset='University_name', inplace=True)

mean_ielts = df['Minimum_IELTS_score'].mean()
df['Minimum_IELTS_score'].fillna(mean_ielts, inplace=True)

print(df[['University_name', 'Minimum_IELTS_score']].head())

# Split the 'Student_enrollment' column into two columns
split_enrollment = df['Student_enrollment'].astype(str).str.split('-', n=1, expand=True)

# Assign the new columns
df['Student_enrollment_Lower_Bound'] = pd.to_numeric(split_enrollment[0], errors='coerce')
df['Student_enrollment_Upper_Bound'] = pd.to_numeric(split_enrollment[1].str.replace(',', ''), errors='coerce')

# Check the outcome: print the first 5 rows
print(
    df[['Student_enrollment_Lower_Bound', 'Student_enrollment_Upper_Bound', 'Student_enrollment']].head().to_markdown())
