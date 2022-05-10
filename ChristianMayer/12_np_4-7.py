import numpy as np


# data: share prices, company - row
data = np.array([[25, 27, 29, 30],
                 [1, 5, 3, 2],
                 [12, 11, 8, 3],
                 [2, 6, 2, 2],
                 [1, 1, 2, 2]])


print([(i, np.var(data[i, :])) for i in range(len(data))])
min_var_row = min([(i, np.var(data[i, :])) for i in range(len(data))], key=lambda x: x[1])


print('')
print(f'Indeks wiersza: {min_var_row[0]}')
print(f'Wartości: {data[min_var_row[0]]}')
print(f'Wariancja (najniższa): {min_var_row[1]}')
