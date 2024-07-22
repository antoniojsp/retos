import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV files into Pandas Dataframes
df_february = pd.read_csv("SOLDFOOD2023 - Winter.xlsx - FEBRUARY.csv")
df_january = pd.read_csv("SOLDFOOD2023 - Winter.xlsx - JANUARY.csv")

# Display the first 5 rows of each DataFrame
print("First 5 rows of df_february:")
print(df_february.head().to_markdown(index=False, numalign="left", stralign="left"))

print("\nFirst 5 rows of df_january:")
print(df_january.head().to_markdown(index=False, numalign="left", stralign="left"))

# Get information about the columns in each of the DataFrames
print("\nInformation about df_february:")
print(df_february.info())

print("\nInformation about df_january:")
print(df_january.info())

# Make the row at index 3 in df_january and df_february the header row
df_january.columns = df_january.iloc[2]
df_february.columns = df_february.iloc[2]

# Remove rows above the header row for both dataframes
df_january = df_january.iloc[3:].copy()
df_february = df_february.iloc[3:].copy()

# Convert the `QUANTITY` column  to numeric after removing '.'
df_january['QUANTITY'] = df_january['QUANTITY'].astype(str).str.replace('.', '', regex=False)
df_january['QUANTITY'] = pd.to_numeric(df_january['QUANTITY'], errors='coerce')
df_february['QUANTITY'] = df_february['QUANTITY'].astype(str).str.replace('.', '', regex=False)
df_february['QUANTITY'] = pd.to_numeric(df_february['QUANTITY'], errors='coerce')

# Add a column `month` with `'January'` for `df_january` and `'February'` for `df_february`
df_january['Month'] = 'January'
df_february['Month'] = 'February'

# Combine df_january and df_february into one dataframe
df_combined = pd.concat([df_january, df_february])

# Display the first 5 rows of the combined DataFrame
print("First 5 rows of df_combined:")
print(df_combined.head().to_markdown(index=False, numalign="left", stralign="left"))


# GROUP the dataframe by `GROUP` and `MONTH` and calculate the mean `QUANTITY` for each group for each month, save in a new dataframe (`df_grouped`) and reset index
df_grouped = df_combined.groupby(['GROUP', 'Month'])[['QUANTITY']].mean().reset_index()

# GROUP the dataframe by `GROUP` and calculate the mean `QUANTITY` across all months, save in a new dataframe (`df_grouped_all`) and reset index
df_grouped_all = df_combined.groupby(['GROUP'])[['QUANTITY']].mean().reset_index()

# Rename the `QUANTITY` column in `df_grouped` to `AVG_QTY_SOLD`
df_grouped = df_grouped.rename(columns={"QUANTITY": "AVG_QTY_SOLD"})

# Print `df_grouped`
print(df_grouped.to_markdown(index=False))

# Rename the `QUANTITY` column in `df_grouped_all` to `OVERALL_AVG_QTY_SOLD`
df_grouped_all = df_grouped_all.rename(columns={"QUANTITY": "OVERALL_AVG_QTY_SOLD"})

# Print `df_grouped_all`
print(df_grouped_all.to_markdown(index=False))