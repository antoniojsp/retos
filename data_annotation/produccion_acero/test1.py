import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('produccion_acero.csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Get all unique values from `c.costo`
unique_values = df['c.costo'].unique()

# Check the number of unique values in `c.costo`
if len(unique_values) > 50:
  # If there are too many unique values, sample the top 50
  top_occuring_values = df['c.costo'].value_counts().head(50).index.tolist()
  print(top_occuring_values)
else:
  # Otherwise print all unique valus in `c.costo`
  print(unique_values)

import altair as alt

# Group by `c.costo` and calculate the sum of `total producido` and `merma rec.`
df_plot = df.groupby('c.costo')[['total producido', 'merma rec.']].sum().reset_index()

# Create a scatter plot
chart = alt.Chart(df_plot).mark_circle(size=60).encode(
    x='total producido',
    y='merma rec.',
    tooltip=['c.costo', 'total producido', 'merma rec.']
).properties(
    title='Relationship between Total Produced and Loss Recovered by Cost Center'
).interactive()

chart.save('total_produced_vs_loss_recovered_scatter_plot.json')

# Print the resultant data.
print(df_plot.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df_plot.info())