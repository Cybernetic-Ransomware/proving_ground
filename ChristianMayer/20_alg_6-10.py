"""
Fibonacci numbers
"""

from functools import reduce


n = 25

fibs = reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (n-2), [0, 1])


print(fibs)
