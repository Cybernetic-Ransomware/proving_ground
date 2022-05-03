import numpy as np
from sklearn import tree

# data: percent rate in math, language and creativity
data = np.array([[90, 50, 60, 'TI'],
                 [10, 80, 10, 'Linguistics'],
                 [50, 70, 90, 'Art']])


tree_ = tree.DecisionTreeClassifier().fit(data[:, :-1], data[:, -1])

prediction = tree_.predict([[80, 60, 50]])
print(prediction)

prediction = tree_.predict([[30, 70, 90]])
print(prediction)
