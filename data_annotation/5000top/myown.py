import pandas as pd

# Read Excel file into a Pandas ExcelFile object
eu = pd.read_excel('population_and_age.xlsx', sheet_name="Europe")
asia = pd.read_excel('population_and_age.xlsx', sheet_name="Asia")
s_america = pd.read_excel('population_and_age.xlsx', sheet_name="South America")

eu.to_csv ("europe.csv", index = None, header=True)
asia.to_csv ("asia.csv", index = None, header=True)
s_america.to_csv ("s_america.csv", index = None, header=True)
print(eu)
europe_csv = pd.read_csv('europe.csv')
asia_csv = pd.read_csv('asia.csv')
south_scv = pd.read_csv('s_america.csv')
# print(eu)
age = 0
countries = 0
population = 0
for i, val in europe_csv.iterrows():
    countries+=1
    age += val["Average Age (Years)"]
    population += val["Population (Million)"]

for i, val in asia_csv.iterrows():
    countries+=1
    age += val["Average Age (Years)"]
    population += val["Population (Approx.)"]/1000000
for i, val in south_scv.iterrows():
    countries+=1
    age += val["Average Age"]
    population += val["Population"]/1000000


print(age, countries, population)
print(f"Average age: {age/countries}")
print(f"Average pop: {population/countries}")



