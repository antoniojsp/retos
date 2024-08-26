import pandas as pd

df = pd.read_csv('log.csv')

print(df[(df[' Average'] >= 68) & (df[' Average'] <= 71)].to_string())
df[' Precipitation'] = df[' Precipitation'].replace('T', '0.00')
df[' Precipitation'] = pd.to_numeric(df[' Precipitation'], errors='coerce')

print(df[(df[' Precipitation'] > 0)].to_string())
