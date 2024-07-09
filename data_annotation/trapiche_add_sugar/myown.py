import pandas as pd

df = pd.read_csv('trapiche_ingenio_nv.csv')
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))
suma = df["Azucar"].sum()

print(f"The total amount of 'Azucar' produces was {suma}.")