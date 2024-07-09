import pandas as pd

df = pd.read_csv('Retail Store Performance and Capacity Metrics - EXO2E Crypto - cccvvv.tsv', delimiter='\t')
df["Installed Capacity Difference"] = df["Installed Capacity 20"] - df["Installed Capacity 30"]
# print(df.head())
cols = list(df.columns)
# print(cols)
cols.insert(cols.index("Installed Capacity 30") + 1, cols.pop(cols.index("Installed Capacity Difference")))
df = df[cols]
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))
df.to_csv("retail_store_performance_installed_difference.csv", index=False)