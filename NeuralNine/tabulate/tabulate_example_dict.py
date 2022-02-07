from tabulate import tabulate


table_data = {'Name': ['Alex', 'Kate', 'Ralph'],
              'Height': [1.8, 1.7, 1.66],
              'Gender': ['M', 'F', 'M'],
              'Occupation': ['Space-marine Sergeant', 'Maintenance Engineer', 'Quartermaster']}

table_format = ['simple', 'psql', 'plain', 'fancy_grid']


def separator(length):
    print()
    print('-' * length)
    print()


separator(50)
print(table_data)

separator(50)
for k, v in table_data.items():
    print(k, end='\t')
    print(v)

for layout in table_format:
    separator(50)
    print(f'{layout = }')
    print(tabulate(table_data, headers='keys', tablefmt=layout, showindex='always'))
