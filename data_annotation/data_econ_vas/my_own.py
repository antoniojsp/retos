import pandas as pd


df = pd.read_csv('DATA_ECOM_VAS_v1-.xlsx-Grossreport.csv')

payment= df.groupby('Payment System Name')['Order'].nunique().idxmax()
print(payment)
max = df.groupby('Payment System Name')['Order'].nunique() # group by payment service
print(payment, max[payment])