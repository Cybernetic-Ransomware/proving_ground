from tabulate import tabulate


table_data = [['Name', 'Height', 'Gender', 'Occupation'],
              ['Alex', 1.8, 'M', 'Space-marine Sergeant'],
              ['Kate', 1.7, 'F', 'Maintenance Engineer'],
              ['Ralph', 1.66, 'M', 'Quartermaster']]

table_format = ['simple', 'psql', 'plain', 'fancy_grid']


def separator(length):
    print()
    print('-' * length)
    print()


separator(50)
print(table_data)

separator(50)
for row in table_data:
    for col in row:
        print(col, end=' ')
    print()

for layout in table_format:
    separator(50)
    print(f'{layout = }')
    print(tabulate(table_data, headers='firstrow', tablefmt=layout))

with open('mytable.html', 'w') as f:
    f.write(tabulate(table_data, headers='firstrow', tablefmt='html'))

with open('mytable.tex', 'w') as f:
    f.write(tabulate(table_data, headers='firstrow', tablefmt='latex'))
