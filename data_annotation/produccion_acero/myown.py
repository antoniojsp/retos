import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('produccion_acero.csv')

print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

import pandas as pd
import matplotlib.pyplot as plt

grouped_sum = df.groupby('c.costo').sum()
print(grouped_sum)

# # Sample data
list1 = grouped_sum["      Cant. Producida"]
list2 = grouped_sum["merma rec."]

# Create a DataFrame
df = pd.DataFrame({
    'Cant. Producida': list2,
    'merma rec': list1
})

import pandas as pd
import matplotlib.pyplot as plt

# Plot the data
plt.plot(df['Cant. Producida'], df['merma rec'], marker='o', linestyle='None')
plt.title('X vs Y Plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True)
plt.show()