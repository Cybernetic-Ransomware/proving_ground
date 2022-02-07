from tabulate import tabulate
import numpy as np
import pandas as pd


table_data = {'Name': ['Alex', 'Kate', 'Ralph'],
              'Height': [1.8, 1.7, 1.66],
              'Gender': ['M', 'F', 'M'],
              'Occupation': ['Space-marine Sergeant', 'Maintenance Engineer', 'Quartermaster']}

table_format = ['simple', 'psql', 'plain', 'fancy_grid']

df = pd.DataFrame(table_data)


def separator(length):
    print()
    print('-' * length)
    print()


separator(50)
print(df)


for layout in table_format:
    separator(50)
    print(f'{layout = }')
    print(tabulate(df, headers='keys', tablefmt=layout, showindex="always"))
