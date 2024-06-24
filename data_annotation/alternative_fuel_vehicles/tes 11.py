import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('Alternative Fuel Vehicles US.csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Filter the data on `Category` and `Drivetrain`
df_filtered = df[(df['Category'].isin(['Sedan/Wagon', 'SUV'])) & (df['Drivetrain'] == 'AWD')]

# Group by `Category` and compute the mean of `Conventional Fuel Economy Combined`
df_grouped = df_filtered.groupby('Category')['Conventional Fuel Economy Combined'].mean()

# Sort in descending order of mean `Conventional Fuel Economy Combined`
df_grouped = df_grouped.sort_values(ascending=False)

# Print the results
print(df_grouped.to_markdown(numalign="left", stralign="left"))