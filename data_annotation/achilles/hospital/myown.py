import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('Hospital_Survey_Data_Alcohol_Drug_Abuse 2.csv', skiprows=[0])

df_filter = df[df["Hospital Rating"] > 3].sort_values(by="Hospital Rating")

with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.expand_frame_repr', False):
    print(df_filter)