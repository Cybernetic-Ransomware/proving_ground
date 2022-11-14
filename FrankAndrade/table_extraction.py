import pandas as pd


df = pd.read_csv('https://otwartedane.gdynia.pl/portal/data/city/1/2/data.csv')
df.rename(columns={'day': 'dzien'}, inplace=True)
print(df.head())
