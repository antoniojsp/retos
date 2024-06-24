import pandas as pd


def remove_cities_less_10000(file:str):
    df = pd.read_csv(file)
    for i, val in df.iterrows():
        if int(val["Population"].replace(",","")) < 10000:
            df = df.drop(i)


print(remove_cities_less_10000("population_ca.csv"))