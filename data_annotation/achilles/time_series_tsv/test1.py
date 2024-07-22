import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the TSV file into a DataFrame
df = pd.read_csv('Invoices Dic - Facturas.tsv', sep='\t')

# Display the first 5 rows
print(df.head())

# Print the column names and their data types
print(df.info())

import matplotlib.pyplot as plt

# Remove ',' from `Amount Untaxed` and convert it to numeric
df['Amount Untaxed'] = df['Amount Untaxed'].str.replace(',', '').astype(float)

# Group by Date and calculate the daily total revenue
grouped = df.groupby('Date')['Amount Untaxed'].sum()

# Print first 5 rows of the grouped dataframe
print(grouped.head())

# Sort by Date
grouped = grouped.sort_index()

# Save grouped DataFrame to a TSV file
grouped.to_csv('time_series.tsv', sep='\t')

# Plot the daily total revenue over time
plt.plot(grouped.index, grouped.values)
plt.title('Daily Total Amount Untaxed')
plt.xlabel('Date')
plt.ylabel('Total Amount Untaxed')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import pandas as pd

# Read the TSV file into a DataFrame with `Date` as the index
df = pd.read_csv('time_series.tsv', sep='\t', index_col='Date', parse_dates=True, infer_datetime_format=True)

# Extract the month from the Date
df['Month'] = df.index.to_series().dt.month

# Group by Month and Date and calculate the daily total revenue
df_agg = df.groupby(['Month', 'Date']).sum().reset_index()
df_agg = df_agg.sort_values(by='Date')

# Display the first 5 rows
print(df_agg.head())

# Print the column names and their data types
print(df_agg.info())

import altair as alt

# Get unique months
months = df_agg['Month'].unique()

# Define a color palette (you can customize this)
color_palette = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']

# Create the base chart
base = alt.Chart(df_agg).encode(
    x=alt.X('Date', axis=alt.Axis(title='Date')),
    y=alt.Y('Amount Untaxed', axis=alt.Axis(title='Total Amount Untaxed')),
    tooltip=['Date', 'Amount Untaxed', 'Month']
)

# Create a line for each month with different colors
lines = alt.layer(*[
    base.mark_line(point=True).transform_filter(
        alt.datum.Month == month
    ).encode(
        color=alt.value(color_palette[i]),
        order=alt.Order('Month', sort='ascending')
    )
    for i, month in enumerate(months)
])

# Add a legend and title
chart = (lines + base.mark_point(filled=True, size=100)).properties(
    title='Daily Total Amount Untaxed by Month'
).interactive()
chart.display()
# Save the chart
chart.save('daily_total_amount_untaxed_by_month_line_chart.json')
