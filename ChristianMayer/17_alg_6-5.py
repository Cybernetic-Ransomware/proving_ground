"""
Power set
"""

from functools import reduce


s = {1, 4, 8, 6}

ps = lambda s: reduce(lambda p, x: p + [subset | {x} for subset in p], sorted(s), [set()])

print(ps(s))
