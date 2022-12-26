import pandas as pd
import matplotlib.pyplot as plt

from plotnine import *
# from plotnine.data import diamonds


df = pd.DataFrame({
    'x': [18, 2, 6, 15, 6, 8, 39, 33, 15],
    'y': [12, 25, 16, 2, 2.4, 4.5, 5, 22, 8.8],
    'group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C']
})

# p = (
#     ggplot(df)
#     + aes(x='x', y='y')
#     + geom_point()
#     + geom_smooth(method='lm')
# )

# p = (
#     ggplot(df)
#     + aes(x='x', y='y')
#     + geom_point()
#     + geom_smooth(span=.7)
# )

p = (
    ggplot(df)
    + aes(x='x', y='y')
    + geom_point()
    + facet_wrap('group')

)

p.draw()
plt.show()
