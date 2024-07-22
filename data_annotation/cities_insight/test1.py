import pandas as pd

# Read the csv file
df = pd.read_csv("Cities with the Best Work-Life Balance 2022.csv")

# Display the first 5 rows
print(df.head())

# Display column names and their types
print(df.info())

import altair as alt

# Aggregate and calculate metrics
total_score_stats = df['TOTAL SCORE'].agg(['mean', 'median', 'min', 'max'])

# Display outputs
print(total_score_stats)

# Visualize the data
chart = alt.Chart(df).mark_bar().encode(
    alt.X('TOTAL SCORE:Q', bin=True),
    y='count()',
    tooltip=[alt.Tooltip('TOTAL SCORE:Q', bin=True), 'count()']
).properties(title='Histogram of Total Score').interactive()

chart.save('total_score_histogram.json')
