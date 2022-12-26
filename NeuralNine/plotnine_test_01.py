# import pandas as pd
import matplotlib.pyplot as plt

from plotnine import *
from plotnine.data import diamonds


df = diamonds
# print(df)

# p = (
#     ggplot(df)
#     + aes(x='cut', y='price', fill='cut')
#     + geom_bar(stat='identity')
# )

# p = (
#     ggplot(df)
#     + aes(x='cut', y='price')
#     + geom_boxplot()
# )

p = (
    ggplot(df)
    + aes(x='price')
    + geom_histogram()
)


p.draw()
plt.show()
