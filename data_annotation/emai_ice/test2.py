import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
emails_df = pd.read_csv('ice_email_replies-ice_email_replies.csv')

# Extract hour from processedAt column
emails_df['processedAt'] = pd.to_datetime(emails_df['processedAt'])
# emails_df['hour'] = emails_df['processedAt'].dt.hour
#
# # Find the hour with the most emails received
# most_emails_hour = emails_df['hour'].value_counts().idxmax()
# most_emails_hour_count = emails_df['hour'].value_counts().max()
#
# most_emails_hour, most_emails_hour_count