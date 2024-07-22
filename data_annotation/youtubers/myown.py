import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('top_200_youtubers.csv')
unique_usernames = df[df["Country"] == "US"]["username"].unique()
unique_usernames_df = pd.DataFrame(unique_usernames, columns=["username"])
unique_usernames_df.to_csv('youtubers.tsv', sep="\t", index=False)