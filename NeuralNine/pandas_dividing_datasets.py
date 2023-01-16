import pandas as pd


# df = pd.read_csv('./ewp_dsh_zgony_po_szczep_202301110922.csv', encoding_errors='ignore', sep=';')  # all 88325 rows
# df = pd.read_csv('./ewp_dsh_zgony_po_szczep_202301110922.csv', encoding_errors='ignore', sep=';', nrows=10000)  # first 10 000 rows
# df = pd.read_csv('./ewp_dsh_zgony_po_szczep_202301110922.csv', encoding_errors='ignore', sep=';', nrows=10000, skiprows=10000)  # second 10 000 rows but without headers!
#
# df = pd.read_csv('./ewp_dsh_zgony_po_szczep_202301110922.csv', encoding_errors='ignore', sep=';', nrows=10000, skiprows=10000)
# df.columns = list(pd.read_csv('./ewp_dsh_zgony_po_szczep_202301110922.csv', encoding_errors='ignore', sep=';', nrows=1))
#
# print(df.info())
# print(df.head())
#
#
# df['min_age'] = df['kat_wiek'].str.split('-').str[0]
# df['min_age'] = df['min_age'].str.replace(r'\D', '', regex=True).astype(int)
# print((df.loc[df['min_age'] >= 80]))


counter = 0
col_names = list(pd.read_csv('./ewp_dsh_zgony_po_szczep_202301110922.csv', encoding_errors='ignore', sep=';', nrows=1))

for chunk in pd.read_csv('./ewp_dsh_zgony_po_szczep_202301110922.csv', encoding_errors='ignore', sep=';', chunksize=1000):
    chunk.columns = col_names
    chunk['min_age'] = chunk['kat_wiek'].str.split('-').str[0]
    chunk['min_age'] = chunk['min_age'].str.replace(r'\D', '', regex=True).replace(r'', '0', regex=False).astype(int)
    print((chunk.loc[chunk['min_age'] >= 80]))
