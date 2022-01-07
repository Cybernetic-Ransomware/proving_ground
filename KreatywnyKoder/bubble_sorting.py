from functools import wraps
from random import sample
from time import time


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Total execution time: {end_ if end_ > 0 else 0} ms")
            print('---')
    return _time_it


array = sample(range(1, 10000), 3000)


@measure
def simple_sort(w_array):
    count = 0
    print(w_array[0:10])

    for j in range(len(w_array)):
        for i in range(len(w_array) - 1):
            count += 1
            if w_array[i] > w_array[i + 1]:
                w_array[i], w_array[i + 1] = w_array[i + 1], w_array[i]

    print(w_array[0:10])
    print(f'Count of iterations: {count}')


@measure
def improved_sort(w_array):
    swapped = True
    count = 0
    print(w_array[0:10])

    while swapped:
        swapped = False
        for i in range(len(w_array) - 1):
            count += 1
            if w_array[i] > w_array[i + 1]:
                w_array[i], w_array[i + 1] = w_array[i + 1], w_array[i]
                swapped = True

    print(w_array[0:10])
    print(f'Count of iterations: {count}')


@measure
def second_improved_sort(w_array):
    swapped = True
    temp = 0
    count = 0
    print(w_array[0:10])

    while swapped:
        swapped = False
        for i in range(len(w_array) - 1 - temp):
            count += 1
            if w_array[i] > w_array[i + 1]:
                w_array[i], w_array[i + 1] = w_array[i + 1], w_array[i]
                swapped = True
        temp += 1

    print(w_array[0:10])
    print(f'Count of iterations: {count}')


if __name__ == '__main__':
    simple_sort(array.copy())
    improved_sort(array.copy())
    second_improved_sort(array.copy())
