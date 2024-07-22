import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('Chainmaille_by_Yael_– Customer_Data_(2023).csv')
print("#  Number of records, column names, data types  #")
print(df.info())

rows_with_nan = df[df.isna().any(axis=1)]
print("#  Rows with missing or NaN values:  #")

print("#  ouliers  #")
df["Price"] = df["Price"].apply(lambda x: int(x[1:]))


Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["Price"] < lower_bound) | (df["Price"] > upper_bound)]

print("Outliers in the '{}' column:".format("Price"))
print(outliers)