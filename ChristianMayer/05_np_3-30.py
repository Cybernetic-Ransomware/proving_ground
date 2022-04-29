from itertools import combinations

import numpy as np


basket = np.array([[0, 1, 1, 0],
                   [0, 0, 0, 1],
                   [1, 1, 0, 0],
                   [0, 1, 1, 1],
                   [1, 1, 1, 0],
                   [0, 1, 1, 0],
                   [1, 1, 0, 1],
                   [1, 1, 1, 1]])


# copurchases = [(i, j, np.sum(basket[:, i] + basket[:, j] == 2)) for i in range(4) for j in range(i+1, 4)]
copurchases = [(i, j, np.sum(basket[:, i] + basket[:, j] == 2)) for i, j in list(combinations([0, 1, 2, 3], 2))]

result = max(copurchases, key=lambda x: x[2])

print(f'The most frequently purchased items together are: {result[:2]}, '
      f'out of the number of joint purchases equal to: {result[2]}')


# print('\nVerification:')
#
# print([(i, j) for i in range(4) for j in range(i+1, 4)])
# print(list(combinations([0, 1, 2, 3], 2)))
#
# print(copurchases)
