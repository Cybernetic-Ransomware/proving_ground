import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


prices = np.array([255, 257, 259])
n = len(prices)

model = LinearRegression().fit(np.arange(n).reshape((n, 1)), prices)


predictions = model.predict([[3], [4]])


print(np.arange(n))
print('')
print(np.arange(n).reshape((n, 1)))
print('')

print(predictions)
print('')


# x = np.arange(n + len(predictions))
# y = np.append(prices, predictions)

x = np.arange(n)
y = prices
x1 = np.arange(len(predictions)) + n
y1 = predictions

print(x)
print(y)
print(x1)
print(y1)


def sketch_chart(data_x, data_y, pred_x1, pred_y1):
    plt.plot(data_x, data_y, marker='o', color='orange', label='data')
    plt.plot(pred_x1, pred_y1, marker='o', color='red', label='predictions')
    plt.xlabel("Time")
    plt.ylabel("Prices")
    plt.title("Value chart")
    plt.legend()
    plt.grid()
    plt.show()


sketch_chart(x, y, x1, y1)
