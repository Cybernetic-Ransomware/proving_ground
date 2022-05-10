import numpy as np
from sklearn import svm


# data: percent rate in math, language and creativity
data = np.array([[90, 50, 60, 'TI'],
                 [100, 10, 20, 'TI'],
                 [0, 10, 25, 'Failure'],
                 [10, 80, 10, 'Linguistics'],
                 [40, 90, 30, 'Linguistics'],
                 [5, 10, 100, 'Art'],
                 [50, 70, 90, 'Art']])


svm_ = svm.SVC().fit(data[:, :-1], data[:, -1])


prediction = svm_.predict([[80, 60, 50]])
print(prediction)

prediction = svm_.predict([[30, 70, 90]])
print(prediction)

prediction = svm_.predict([[30, 30, 60]])
print(prediction)

prediction = svm_.predict([[0, 10, 10]])
print(prediction)
