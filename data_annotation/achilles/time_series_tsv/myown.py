import pandas as pd

df = pd.read_csv('time_series.tsv', sep='\t', index_col='Date', parse_dates=True, infer_datetime_format=True)

df['Month'] = df.index.to_series().dt.month

df = df.groupby(['Month', 'Date']).sum().reset_index()
df = df.sort_values(by='Date')

import pandas as pd
import matplotlib.pyplot as plt
df.plot(x='Date', y='Amount Untaxed', kind='line', marker='o')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.show()