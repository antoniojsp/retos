import pandas as pd
# It appears the first row contains the column headers, so we should reload the data with proper headers
real_estate_data = pd.read_csv('Buncombe_-_Closed_SFR_-_11_30_23_-_12_30_23_-_Sheet1(1).csv', header=1)

# Calculate the average "Days on Market to Close"
average_days_on_market = real_estate_data['Days on Market to Close'].mean()
print(average_days_on_market)