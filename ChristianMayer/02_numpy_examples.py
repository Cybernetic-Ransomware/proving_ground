import numpy as np


adam = [112000, 140000, 112800]
eva = [90000, 105000, 130000]
jack = [99000, 89000, 95000]

salaries = np.array([adam, eva, jack])
taxation = np.array([[0.12, 0.33, 0.28],
                     [0.12, 0.25, 0.20],
                     [0.12, 0.10, 0.12]])

sum_taxation = np.sum(salaries * taxation)
print(f'{sum_taxation = :.2f}')

avg_taxation = np.sum(salaries * taxation) / (len(salaries[0]) * len(taxation[0]))
print(f'{avg_taxation = :.2f}')

max_income = np.max(salaries - salaries * taxation)
person = ['Adam', 'Eva', 'Jack'][int(np.where(salaries - salaries * taxation == max_income)[0][0])]

print(f'{max_income = :.2f} reached by {person}')

print(f'Last year taxes value: {sum((salaries * taxation)[:, 2]):.2f} PLN')

print(salaries.shape)
print(salaries.ndim)

