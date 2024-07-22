# Let's start by loading the uploaded CSV file to understand its structure and contents.
import pandas as pd

# Load the CSV file
df = pd.read_csv('last60.csv')

# Display the first few rows of the dataframe to understand its structure
df.head()

# Step 1: Calculate the average cost for each unique brand
average_cost_per_brand = df.groupby('Brand')['Cost'].mean().reset_index()

# Step 2: Find out which brand has the highest quantity available
highest_qty_brand = \
df.groupby('Brand')['QtyAvail'].sum().reset_index().sort_values(by='QtyAvail', ascending=False).iloc[0]

# Step 3: Check if the acquired date for the brand with the highest quantity available is "11/29/2023"
acquired_date_check = df[(df['Brand'] == highest_qty_brand['Brand']) & (df['AcquiredDate'] == "11/29/2023")]

print(average_cost_per_brand, highest_qty_brand, not acquired_date_check.empty)
