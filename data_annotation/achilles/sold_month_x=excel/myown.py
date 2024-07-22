import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

feb_data = pd.read_csv("SOLDFOOD2023 - Winter.xlsx - FEBRUARY.csv", skiprows=[0, 1, 2])
january_data = pd.read_csv("SOLDFOOD2023 - Winter.xlsx - JANUARY.csv", skiprows=[0, 1, 2])

january_data['QUANTITY'] = january_data['QUANTITY'].astype(str).str.replace('.', '', regex=False)
january_data['QUANTITY'] = pd.to_numeric(january_data['QUANTITY'])
feb_data['QUANTITY'] = feb_data['QUANTITY'].astype(str).str.replace('.', '', regex=False)
feb_data['QUANTITY'] = pd.to_numeric(feb_data['QUANTITY'])

january_data['Month'] = 'January'
feb_data['Month'] = 'February'

new_df = pd.concat([january_data, feb_data])
new_df = new_df.groupby(['GROUP', 'Month'])[['QUANTITY']].mean().reset_index()
print(new_df)