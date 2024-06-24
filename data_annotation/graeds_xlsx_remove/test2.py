import pandas as pd

# Load the Excel file
grades_path = 'grades.xlsx'
grades_df = pd.read_excel(grades_path)

# Check the initial structure of the dataframe to understand the data better
print(grades_df.head())
