import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('produccion_acero.csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

import altair as alt

# Aggregate the data by `c.costo`, summing `total producido` and `    Valor Est. Merma`.
df_agg = df.groupby('c.costo')[['total producido', '    Valor Est. Merma']].sum().reset_index()

# Create a simple scatterplot with `total producido` on the x-axis and `    Valor Est. Merma` on the y-axis.
chart = alt.Chart(df_agg).mark_circle().encode(
    x=alt.X('total producido', title='Total producido'),
    y=alt.Y('    Valor Est. Merma', title='Valor estimado merma'),
    tooltip=['c.costo', 'total producido', '    Valor Est. Merma']
).properties(
    title='Relationship between total produced and loss recovered by cost center'
).interactive()

chart.save('total_producido_vs_valor_est_merma_scatterplot.json')
