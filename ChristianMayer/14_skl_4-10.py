import numpy as np
from sklearn.ensemble import RandomForestClassifier


# data: percent rate in math, language and creativity
data = np.array([[90, 50, 60, 'TI'],
                 [100, 10, 20, 'TI'],
                 [10, 80, 10, 'Linguistics'],
                 [40, 90, 30, 'Linguistics'],
                 [5, 10, 100, 'Art'],
                 [50, 70, 90, 'Art']])


forest_ = RandomForestClassifier(n_estimators=10).fit(data[:, :-1], data[:, -1])


prediction = forest_.predict([[80, 60, 50],
                              [30, 70, 90],
                              [30, 30, 60],
                              [30, 80, 10]])

print(prediction)
