import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv("Book_Sales.csv")

df_filter = df[(df["Date Order"] == "10/12/2020") & (df["Order ID"] == 242113196)]
print(df_filter[" Total Sales"])