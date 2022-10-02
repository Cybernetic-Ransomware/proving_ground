import tabula


tables = tabula.read_pdf('WFRP_4e_Shrines_of_Sigmar.pdf', pages='all')
df = tables[0]
print(df.head())
