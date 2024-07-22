import pandas as pd
from tabulate import tabulate

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)

# Read the CSV files into Pandas Dataframes
df_excel = pd.read_csv('Hospital_Survey_Data_Alcohol_Drug_Abuse 2.csv', skiprows=1)
df_csv = pd.read_csv('Hospital_Survey_Data_Speticemia.csv', skiprows=1)

def join_location(csv_file):
    csv_file_loc = csv_file[["Provider City", "Provider State", "Provider Zip Code"]]
    location = []
    for i, val in csv_file_loc.iterrows():
        location.append(f'{val["Provider City"]} {val["Provider State"]} {val["Provider Zip Code"]}')

    csv_file["Location"] = location
    return csv_file


print(tabulate(join_location(df_csv).head(), headers='keys', tablefmt='psql'))
print(tabulate(join_location(df_excel).head(), headers='keys', tablefmt='psql'))

