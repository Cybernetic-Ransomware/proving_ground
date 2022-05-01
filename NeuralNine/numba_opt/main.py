import math
import random
from time import time

from numba import jit
import numpy as np


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


@timer_func
def example_function(n):
    z = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        z += math.sqrt(x ** 2 + y ** 3)
    return z


example_function(10_000_000)
example_function(10_000_000)


@timer_func
@jit(nopython=True)
def example_function(n):
    z = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        z += math.sqrt(x ** 2 + y ** 3)
    return z


print('\nNow with numpa:')
example_function(10_000_000)
example_function(10_000_000)


@timer_func
def example_function_with_numpy(n):
    z = np.zeros((n, n))
    for i in range(n):
        x = np.random.rand(n, n)
        y = np.random.rand(n, n)
        z += np.sqrt(x ** 2 + y ** 3)
    return z


print('\nTest on numpy arrays:')
example_function_with_numpy(800)
example_function_with_numpy(800)


@timer_func
@jit(nopython=True)
def example_function_with_numpy(n):
    z = np.zeros((n, n))
    for i in range(n):
        x = np.random.rand(n, n)
        y = np.random.rand(n, n)
        z += np.sqrt(x ** 2 + y ** 3)
    return z


print('\nNow with numpa:')
example_function_with_numpy(800)
example_function_with_numpy(800)
