from tabulate import tabulate
import numpy as np


table_data = {'Name': ['Alex', 'Kate', 'Ralph'],
              'Height': [1.8, 1.7, 1.66],
              'Gender': ['M', 'F', 'M'],
              'Occupation': ['Space-marine Sergeant', 'Maintenance Engineer', 'Quartermaster']}

table_format = ['simple', 'psql', 'plain', 'fancy_grid']

data = [[k, *v] for k, v in table_data.items()]
an_array = np.array(data).transpose()


def separator(length):
    print()
    print('-' * length)
    print()


separator(50)
print(an_array)


for layout in table_format:
    separator(50)
    print(f'{layout = }')
    print(tabulate(an_array, headers='firstrow', tablefmt=layout, showindex="never"))
