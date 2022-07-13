from random import sample
from pylab import plot, show


x_vals = sample(range(-100, 100), 200)
x_vals.sort()
y_vals = [x**2 + 2*x + 1 for x in x_vals]

plot(x_vals, y_vals)
show()
