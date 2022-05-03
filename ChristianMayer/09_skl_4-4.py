import numpy as np
from sklearn.neighbors import KNeighborsRegressor


area_to_price = np.array([[35, 120000],
                          [45, 180000],
                          [40, 200000],
                          [35, 140000],
                          [25, 130000],
                          [40, 160000]])

k_nearest_neighbours = KNeighborsRegressor(n_neighbors=3).fit(area_to_price[:, 0].reshape(-1, 1), area_to_price[:, 1])
prediction = k_nearest_neighbours.predict([[30]])

print(prediction)
