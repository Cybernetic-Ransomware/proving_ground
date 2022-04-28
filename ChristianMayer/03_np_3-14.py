import numpy as np

x = np.array(
    [[42, 40, 41, 43, 44, 43],      # Hongkong
     [30, 31, 29, 29, 29, 30],      # New York
     [8, 13, 31, 11, 11, 9],        # Berlin
     [11, 11, 12, 13, 11, 12]])     # Montreal

cities = np.array(['Hongkong', 'New York', 'Berlin', 'Montreal'])

polluted = set(cities[np.nonzero(x > np.average(x))[0]])
print(polluted)
print(np.average(x))
