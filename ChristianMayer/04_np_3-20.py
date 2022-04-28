import numpy as np

tmp = np.array([1, 2, 3, 4, 3, 4, 4,
                5, 3, 3, 4, 3, 4, 6,
                6, 5, 5, 5, 4, 5, 5])

print(tmp)

# print(np.average(tmp.reshape((-1, 7)), axis=1))
#
# print(sum((1, 2, 3, 4, 3, 4, 4))/7)
# print(sum((5, 3, 3, 4, 3, 4, 6,))/7)
# print(sum((6, 5, 5, 5, 4, 5, 5))/7)

tmp[6::7] = np.average(tmp.reshape((-1, 7)), axis=1)
print(tmp)
