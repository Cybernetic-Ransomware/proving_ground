import numpy as np
from bokeh.plotting import figure, show


x = np.random.random(50) * 10
y = np.random.random(50) * 200


p = figure(title="Example charts", x_axis_label='x', y_axis_label='y', background_fill_color='pink')


p.circle(x, y, legend_label='Random points', color='darkgreen', size=10)


show(p)
