import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# 1. Read the CSV file into a DataFrame
df = pd.read_csv("last60.csv")

# mean by cost
brand_aver = df.groupby('Brand')['Cost'].mean()

# highest QtyAvail
brand_cost = df.groupby('Brand')['QtyAvail'].sum()
# print(brand_cost[df.groupby('Brand')['QtyAvail'].sum() == df.groupby('Brand')['QtyAvail'].sum().max()])

df_date = df[(df["AcquiredDate"] == "11/29/2023") & (df["Brand"] == "ALLSTAR PERFORMANCE")]
# print(df_date)

print(df[df["AcquiredDate"] == "11/29/2023"])