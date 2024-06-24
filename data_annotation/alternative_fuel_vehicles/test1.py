
import pandas as pd
from math import isnan
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('Alternative Fuel Vehicles US.csv')
# print(df.to_string())
suv_fuel = [0, 0]
sedan_fuel = [0,0]
for index, val in df.iterrows():
    if val["Drivetrain"] == "AWD":
        if val["Category"] == "SUV" and not isnan(val["Conventional Fuel Economy Combined"]):
            print("SUV", val["Conventional Fuel Economy Combined"])
            suv_fuel[0] += val["Conventional Fuel Economy Combined"]
            suv_fuel[1] += 1
        elif val["Category"] == "Sedan/Wagon" and not isnan(val["Conventional Fuel Economy Combined"]):
            print("Sedan", val["Conventional Fuel Economy Combined"])
            sedan_fuel[0] += val["Conventional Fuel Economy Combined"]
            sedan_fuel[1] += 1

print(f"Sedan economy: {sedan_fuel[0]/sedan_fuel[1]} vs Suv: {suv_fuel[0]/suv_fuel[1]}")