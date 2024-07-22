import pandas as pd

# 1. Read the CSV file into a DataFrame
df = pd.read_csv("last60.csv")

# 2. Display the first 5 rows and all columns
print(df.head())

# 3. Show columns and their types
print(df.info())

# Transform and Aggregate
# 1. Group by 'Brand' and calculate the mean of 'Cost'
avg_cost_by_brand = df.groupby('Brand')['Cost'].mean().reset_index()

# 2. Sort by 'Cost' in descending order and print
avg_cost_by_brand = avg_cost_by_brand.sort_values(by='Cost', ascending=False)
print("Average Cost by Brand (Descending):")
print(avg_cost_by_brand)

# Find Max
# 1. Find the 'Brand' with the highest 'QtyAvail'
brand_with_highest_qty = df.loc[df['QtyAvail'].idxmax(), 'Brand']

# 2. Print the brand
print("\nBrand with Highest QtyAvail:")
print(brand_with_highest_qty)

# Filter and Display
# 1. Filter rows where 'AcquiredDate' is '11/29/2023'
filtered_df = df[df['AcquiredDate'] == '11/29/2023']

# 2. Print the first 5 rows or a message if empty
if not filtered_df.empty:
    print("\nFirst 5 rows with 'AcquiredDate' as '11/29/2023':")
    print(filtered_df.head())
else:
    print("\nNo rows found with 'AcquiredDate' as '11/29/2023'")
# OUTPUT
if not filtered_df.empty:
    print(filtered_df.to_string())
else:
    print("No rows found with 'AcquiredDate' as '11/29/2023'")
