import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('Spotify_2000.csv')
max_index = df['Length (Duration)'].idxmax()
print(df.loc[max_index]["Artist"])