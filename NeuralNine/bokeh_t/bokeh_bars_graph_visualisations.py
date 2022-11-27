import numpy as np
from bokeh.plotting import figure, show


x = np.arange(0, 20, 1)
y = np.random.random(50) * 100


p = figure(title="Example charts", x_axis_label='x', y_axis_label='y', background_fill_color='azure')


p.vbar(x=x, top=y, bottom=0, width=0.8, legend_label='Some bars', color='brown')


show(p)
