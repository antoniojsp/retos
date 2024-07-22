import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df_period2 = pd.read_csv('grades.xlsx - Period 2.csv')

# Display the first 5 rows
print(df_period2.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df_period2.info())

# Filter out rows where `Student` column is empty
df_period2_updated = df_period2[df_period2['Student'].astype(str).str.strip() != '']

# Check if any rows were dropped
if df_period2_updated.shape[0] < df_period2.shape[0]:
    # Save the updated DataFrame to a new CSV file
    df_period2_updated.to_csv('grades_period2_updated.csv', index=False)
    print("Empty rows have been removed and the updated DataFrame has been saved to 'grades_period2_updated.csv'")
else:
    print("No empty rows were found in the 'Student' column.")

