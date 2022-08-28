import math
import time

from joblib import Parallel, delayed
from psutil import cpu_count


RANGE = 14000


def main_01():
    res = [math.factorial(x) for x in range(RANGE)]
    return None


def main_02():
    res = Parallel(n_jobs=2)(delayed(math.factorial)(x) for x in range(RANGE))
    return None


def main_03():
    res = Parallel(n_jobs=4)(delayed(math.factorial)(x) for x in range(RANGE))
    return None


def main_04():
    res = Parallel(n_jobs=-1)(delayed(math.factorial)(x) for x in range(RANGE))
    return None


if __name__ == '__main__':

    for func, cores in {main_01: 1, main_02: 2, main_03: 4, main_04: cpu_count()}.items():
        t1 = time.time()
        func()
        main_04()
        t2 = time.time()
        print(f'Execusion time: {t2 - t1:.4f}s with usage of: {cores} core(s).')
