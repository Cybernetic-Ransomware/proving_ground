import math


n = [5, 1, 0, 4, 9, -1]


factorial_ = lambda x: x * factorial_(x-1) if x > 1 else 1


for number in n:
    print(factorial_(number))
    print(math.factorial(number))
    print('')

# math return ValueError witch negative arguments
# max argument value for math is 998
# factorial_ can take higher values
