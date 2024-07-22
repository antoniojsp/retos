import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('grades.xlsx - Period 2.csv')
df.dropna(subset=['Homework'], inplace=True)
df.dropna(subset=['Midterm'], inplace=True)
df.dropna(subset=['Final Exam'], inplace=True)
df.dropna(subset=['Student'], inplace=True)

print(df)