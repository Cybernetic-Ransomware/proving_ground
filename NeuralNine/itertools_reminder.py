import itertools


# itertools.count - appending generator
"""
for i in range(0, 500, 2):
    print(i)

i = 0
while True:
    print(i)
    i += 2
    if i >= 500:
        break


counter = itertools.count(0, 2)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

print(list(range(0, 500, 2)))
# print(list(counter))            # infinite appending list

"""

# itertools.cycle - infinity-cycle generator
'''
elements = [1, True, 4.2, 'aligator']

# for i in itertools.cycle(elements):
#     print(i)

my_cycle = itertools.cycle(elements)
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
'''

# itertools.product - Cartesian product
'''
numbers_01 = [1, 4, 6]
numbers_02 = [7, 8, 2]

prod = []

for i in numbers_01:
    for j in numbers_02:
        prod.append((i, j))

print(prod)

print(list(itertools.product(numbers_01, numbers_02)))
'''

# itertools.permutations | itertools.combination | itertools.combinations_with_replacement
'''
elements = ['A', 'B', 'C', 'D', 'E']

print(list(itertools.permutations(elements)))
print(len(list(itertools.permutations(elements))))

print(list(itertools.combinations(elements, 2)))
print(len(list(itertools.combinations(elements, 2))))

print(list(itertools.combinations_with_replacement(elements, 2)))
print(len(list(itertools.combinations_with_replacement(elements, 2))))
'''
