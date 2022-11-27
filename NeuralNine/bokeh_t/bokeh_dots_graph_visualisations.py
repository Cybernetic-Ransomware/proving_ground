import numpy as np
from bokeh.layouts import row
from bokeh.plotting import figure, show, curdoc


x = np.random.random(50) * 10
y1 = np.random.random(50) * 200
y2 = np.random.random(50) * 200
y3 = np.random.random(50) * 200


curdoc().theme = 'dark_minimal'

p1 = figure(title="Example charts", x_axis_label='x', y_axis_label='y', background_fill_color='lightgrey')
# p1.width = 400  # to allow sizing_mode arg
p1.height = 600
p1.margin = (10, 20, 10, 20)

p2 = figure(title="Example charts", x_axis_label='x', y_axis_label='y',
            background_fill_color='lightgrey', height=600, margin=(10, 20, 10, 20))

p3 = figure(title="Example charts", x_axis_label='x', y_axis_label='y',
            background_fill_color='lightgrey', height=600, margin=(10, 20, 10, 20))


char_01 = p1.circle(x, y1, legend_label='Random points', color='yellow', size=10)
char_02 = p2.circle(x, y2, legend_label='Random points', color='orange', size=12)
char_03 = p3.circle(x, y3, legend_label='Random points', color='darkgreen', size=8)

# changing chart layout after sketching
#
# char_12 = char_01.glyph
# char_12.size = 20
# char_12.fill_color = 'purple'

show(row(children=[p1, p2, p3], sizing_mode='scale_width'))
