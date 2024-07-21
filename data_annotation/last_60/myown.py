import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('last60.csv')
#
# # Display the first 5 rows
# print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

df["Category Levels"] = df["Category Level 1"] + " - "+  df["Category Level 2"] +" - "+ df["Category Level 3"]


for i in df["Category Levels"]:
    print(i)