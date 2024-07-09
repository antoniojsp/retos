import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('ice_email_replies-ice_email_replies.csv')

# print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
dictionary = {}
for i in df["processedAt"]:
    dictionary[i[11:13]] = dictionary.get(i[11:13], 0) + 1

temp = sorted(dictionary.items(), key=lambda x:x[1], reverse=True)[0]


print(f"The  hour that it has most email is {temp[0]} with {temp[1]} times.")