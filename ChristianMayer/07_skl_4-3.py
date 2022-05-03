import numpy as np
from sklearn.cluster import KMeans


hours_to_wages = np.array([[35, 7000],
                           [45, 6900],
                           [70, 7100],
                           [20, 2000],
                           [25, 2200],
                           [15, 1800]])

kmeans = KMeans(n_clusters=2).fit(hours_to_wages)
centres = kmeans.cluster_centers_

print(centres)
