import numpy as np
from sklearn.linear_model import LogisticRegression


health = np.array([[20, 'healthy'],
                   [10, 'healthy'],
                   [5, 'healthy'],
                   [29, 'healthy'],
                   [29, 'sick'],
                   [50, 'sick'],
                   [88, 'sick']])
model = LogisticRegression().fit(health[:, 0].reshape(-1, 1), health[:, 1])

asked = [[10], [14], [40], [42], [47], [29], [88]]
predictions = model.predict(asked)


print(health[:, 0])
print('')
print(health[:, 0].reshape(-1, 1))
print('')

print([(*a, p) for a, p in zip(asked, predictions)])
print('')


for x in range(60):
    print(f'x={x} -> + {str(model.predict_proba([[x]]))}')
