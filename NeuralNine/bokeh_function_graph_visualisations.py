import numpy as np
from bokeh.plotting import figure, show


x = np.arange(0, 10, 1)

y1 = x ** 3 + 20
y2 = x ** 2 + 2*x + 10
y3 = x ** 4 - 18*x + 5

p = figure(title="Example charts", x_axis_label='x', y_axis_label='y', background_fill_color='lightgrey')

p.line(x, y1, legend_label='First function example', line_width=2, color='yellow')
p.line(x, y2, legend_label='Second function example', line_width=2, color='brown')
p.line(x, y3, legend_label='Third function example', line_width=2, color='orange')

show(p)
