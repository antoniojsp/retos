import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv("Book_Sales.csv")

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Print the column names of the filtered dataframe
# Filter the DataFrame based on `Order ID` and `Date Order`
filtered_df = df[(df['Order ID'] == 242113196) & (df['Date Order'] == '10/12/2020')]

# Get all unique ` Total Sales` values from filtered dataframe
unique_values = filtered_df[' Total Sales'].unique()

# Check the number of unique values in ` Total Sales`
if len(unique_values) > 20:
    # If there are too many unique values, sample the top 20
    top_occuring_values = filtered_df[' Total Sales'].value_counts().head(20).index.tolist()
    print(top_occuring_values)
else:
    # Otherwise print all unique valus in ` Total Sales`
    print(unique_values)
