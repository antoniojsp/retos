import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('Book_Sales.csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Filter the data to the row where `Order ID` is 242113196
filtered_df = df[df['Order ID'] == 242113196]

# Remove '€' and ',' from the column ` Total Sales`
filtered_df[' Total Sales'] = filtered_df[' Total Sales'].astype(str).str.replace(r'[€,]', '', regex=True)

# Convert the column ` Total Sales` to numeric
filtered_df[' Total Sales'] = pd.to_numeric(filtered_df[' Total Sales'])

# Print the value in the column ` Total Sales`
print(
    f"The total sales amount for the order placed on 10/12/2020 with ID 242113196 is: {filtered_df[' Total Sales'][0]}")
