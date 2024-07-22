import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('uk_universities.csv')

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

# Get all unique values from `Student_enrollment`
unique_values = df['Student_enrollment'].unique()

# Check the number of unique values in `Student_enrollment`
if len(unique_values) > 50:
  # If there are too many unique values, sample the top 50
  top_occuring_values = df['Student_enrollment'].value_counts().head(50).index.tolist()
  print(top_occuring_values)
else:
  # Otherwise print all unique valus in `Student_enrollment`
  print(unique_values)

# Extract the first 5 characters of the string as the lower bound and convert it to numeric datatype
df['Student_enrollment_Lower_Bound'] = df['Student_enrollment'].astype(str).str[:5]
df['Student_enrollment_Lower_Bound'] = pd.to_numeric(df['Student_enrollment_Lower_Bound'])

# Extract the last 5 characters of the string as the upper bound and convert it to numeric datatype
df['Student_enrollment_Upper_Bound'] = df['Student_enrollment'].astype(str).str[-5:]
df['Student_enrollment_Upper_Bound'] = pd.to_numeric(df['Student_enrollment_Upper_Bound'])

# Drop the original `Student_enrollment` column
df.drop(columns=['Student_enrollment'], inplace=True)

# Display the first 5 rows
print(df.head())

# Print the column names and their data types
print(df.info())