import matplotlib.pyplot as plt

countries = [
    "China", "India", "United States", "Indonesia", "Pakistan", 
    "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico", 
    "Japan", "Ethiopia", "Philippines", "Egypt", "Vietnam", 
    "DR Congo", "Germany", "Iran", "Turkey", "Thailand", 
    "United Kingdom", "France", "Italy", "Tanzania", "South Africa", 
    "Myanmar", "South Korea", "Colombia", "Kenya", "Spain"
]

populations = [
    1444, 1400, 335, 279, 234, 
    215, 211, 171, 145, 130, 
    126, 115, 111, 106, 99, 
    94, 84, 84, 84, 70, 
    67, 65, 60, 60, 60, 
    55, 52, 51, 50, 47
]

plt.figure(figsize=(10, 5))
plt.bar(countries, populations, color='red')

plt.xticks(rotation=90)

plt.xlabel('Country')
plt.ylabel('Population in millions')
plt.title('Population of Countries')

plt.tight_layout()
plt.show()