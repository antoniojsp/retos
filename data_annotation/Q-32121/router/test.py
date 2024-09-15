import pandas as pd

# Replace 'file.tsv' with the path to your TSV file
df = pd.read_csv('c.tsv', delimiter='\t')

# Display the DataFrame
print(df.to_string())
