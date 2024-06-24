import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('Sales-PrintingOffice2023v1-Sheet1.csv')
print(df.to_string())
print(df.info())
temp = {
        "October":0,
        "November":0
       }

for index, row  in df.iterrows():
    print(row["Final Price"])
    if type(row["Request date"]) == type(""):
        match row["Request date"][-3:]:
            case "Nov":
                temp["November"]+=float(row["Final Price"][1:].replace(",",""))
            case "Oct":
                temp["October"]+=float(row["Final Price"][1:].replace(",",""))

print(temp)