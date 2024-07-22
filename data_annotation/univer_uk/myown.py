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

# print(df[['University_name', 'Minimum_IELTS_score']].head())

grouped_results = df.groupby('Region')['Minimum_IELTS_score'].mean()
# print(grouped_results.to_markdown())
upper_list = []
lower_list = []
for i in df["Student_enrollment"]:
  lower, upper = i.split("-")
  upper_list.append(upper)
  lower_list.append(lower)

df["Student_enrollment_Lower_Bound"] = lower_list
df["Student_enrollment_Upper_Bound"] = upper_list
df.drop(columns=['Student_enrollment'], inplace=True)
print(df.to_string())
# Remove ',' and '-' from the `Student_enrollment` column
df['Student_enrollment'] = df['Student_enrollment'].astype(str).str.replace(',', '').str.replace('-', '')

# Split the `Student_enrollment` column into two columns
df[['Student_enrollment_Lower_Bound', 'Student_enrollment_Upper_Bound']] = df['Student_enrollment'].str.split(' ', expand=True)

# Fill NaN values in `Student_enrollment_Upper_Bound` with `Student_enrollment_Lower_Bound`
df['Student_enrollment_Upper_Bound'] = df['Student_enrollment_Upper_Bound'].fillna(df['Student_enrollment_Lower_Bound'])

# Convert the columns to numeric
df['Student_enrollment_Lower_Bound'] = pd.to_numeric(df['Student_enrollment_Lower_Bound'])
df['Student_enrollment_Upper_Bound'] = pd.to_numeric(df['Student_enrollment_Upper_Bound'])

# Drop the original `Student_enrollment` column
df.drop(columns=['Student_enrollment'], inplace=True)

# Display the first 5 rows
print(df.head())

# Print the column names and their data types
print(df.info())
import numpy as np

# Get all unique non-numeric values from `Student_enrollment`
non_numeric_student_enrollment_value = df[pd.to_numeric(df['Student_enrollment'], errors='coerce').isna()][
  'Student_enrollment'].unique()

if (len(non_numeric_student_enrollment_value) > 20):
  # Sample 20 of them if there are too many unique values
  print(
    f"Non numeric values in Student_enrollment : {np.random.choice(non_numeric_student_enrollment_value, 20, replace=False)}")
else:
  # Otherwise print all unique non-numeric values from `Student_enrollment`
  print(f"Non numeric values in Student_enrollment : {non_numeric_student_enrollment_value}")
