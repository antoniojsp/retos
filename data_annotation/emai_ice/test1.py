import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('ice_email_replies-ice_email_replies.csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Convert `processedAt` to datetime, inferring the format individually
df['processedAt'] = pd.to_datetime(df['processedAt'], format='mixed')

# Extract hour from `processedAt`
df['hour'] = df['processedAt'].dt.hour

# Group by `hour` and count the number of emails
df_result = df.groupby('hour').size().to_frame(name='email_count')

# Sort by `email_count` in descending order
df_result = df_result.sort_values(by='email_count', ascending=False)

# Display the top 3 hours
print("The time where most emails are received:\n")
print(df_result.head(3).to_markdown(numalign="left", stralign="left"))
