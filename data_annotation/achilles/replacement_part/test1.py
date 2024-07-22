import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.read_csv('dataset.csv')

print(df.head().to_markdown(index=False, numalign='left', stralign="left"))

print(df['Replacement Part Number'].value_counts().to_markdown())

count = len(df[(df['Replacement Part Number'].notnull()) & (df['Replacement Part Number'] != 'NOT AVAILABLE') & (
            df['Replacement Part Number'] != 'NOT APPLICABLE')])
print(f"Number of rows with valid replacement part number: {count}")

# Filter the DataFrame to only include rows where 'Insufficient Spares' is greater than 0
insufficient_spares_df = df[df['Insufficient Spares'] > 0]

# Count the number of rows with insufficient spares
count_insufficient_spares = len(insufficient_spares_df)

# Print the results
print(f"Number of rows with insufficient spares: {count_insufficient_spares}")

