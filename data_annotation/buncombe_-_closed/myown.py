from math import isnan

import pandas as pd

df = pd.read_csv('Buncombe_-_Closed_SFR_-_11_30_23_-_12_30_23_-_Sheet1(1).csv', skiprows=1)
temp = df["Days on Market to Close"].sum()

sum = 0
count = 0
for i, val in df.iterrows():
    if not isnan(val["Days on Market to Close"]):
        sum += val["Days on Market to Close"]
        count+=1
print(f"Average = {sum/count}")