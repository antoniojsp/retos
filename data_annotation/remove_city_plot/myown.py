import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df_ny = pd.read_csv('population_ny.csv')
df_ma = pd.read_csv('population_ma.csv')

# Function to drop rows with population less than a given limit
def drop_less_than(dataframe, limit):
    dataframe['Population'] = dataframe['Population'].str.replace(",", "").astype(int)
    filtered_df = dataframe[dataframe['Population'] >= limit]
    return filtered_df

# Apply the filtering function
filtered_ny = drop_less_than(df_ny, 100000)
filtered_ma = drop_less_than(df_ma, 100000)

# Print the filtered data
print(filtered_ny)
print(filtered_ma)

def plot_population(dataframe, state_name):
    plt.figure(figsize=(10, 5))
    dataframe.plot(kind='bar', x='City', y='Population', legend=False)
    plt.xlabel('City')
    plt.ylabel('Population')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Plot the filtered data
plot_population(filtered_ny, "New York")
plot_population(filtered_ma, "Massachusetts")





# df_ny['Population'] = pd.to_numeric(df_ny['Population'].str.replace(',', ''))
# df_ma['Population'] = pd.to_numeric(df_ma['Population'].str.replace(',', ''))
#
# df_ny[df_ny['Population'] >= 100_000].to_csv('population_ny_filtered1.csv', index=False)
# df_ma[df_ma['Population'] >= 100_000].to_csv('population_ma_filtered1.csv', index=False)
#
#
