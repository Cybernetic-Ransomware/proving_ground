"""
Sieve of Eratosthenes
"""

from functools import reduce


n = 800_000

primes_lover_than = sorted(reduce(lambda r, x: r - set(range(x**2, n, x)) if x in r else r,
                                  range(2, int(n**0.5) + 1), set(range(2, n))))


print(primes_lover_than)
