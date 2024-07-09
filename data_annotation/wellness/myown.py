import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the TSV file into a DataFrame
df = pd.read_csv("WELLNESS_COST_2022_CW_V2 - Sheet1.tsv", sep='\t')

# Permanently changes the pandas settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

grouped = (
    df.groupby(['JOB DESC', 'CONCEPT'])[['TOTAL']]
    .sum()
    .unstack('CONCEPT')
    .fillna(0)
)
print(grouped)

# last question
temp = grouped[ (grouped >= 100).all(axis=1) ]
print(temp)
