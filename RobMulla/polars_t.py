import pandas as pd
import polars as pl


r_df = pl.read_csv('https://j.mp/iriscsv')
r_df_2 = pd.read_csv('https://j.mp/iriscsv')


# print(df.head())


# print(r_df.filter(pl.col('sepal_length') > 5)
#       .groupby('species', maintain_order=True)
#       .agg(pl.all().sum()))
#
# print(r_df_2.query('sepal_length > 5').groupby('species').sum())


# df = r_df.lazy()\
#       .filter(pl.col('sepal_length') > 5)\
#       .groupby('species', maintain_order=True)\
#       .agg(pl.all().sum())\
#       .collect()  # wythout will show sheme graph when running on jupyter nb
# print(df)


# print(r_df.columns, end='\n\n')
#
# df = r_df.select(pl.col(['species', 'sepal_length', 'sepal_width'])).head()
# print(df)
#
# df = r_df.select(pl.exclude(['sepal_length', 'sepal_width'])).tail()
# print(df)


# df = r_df.with_columns([
#       pl.col('sepal_length').mean().alias('sepal_length_mean'),
#       (pl.col('sepal_length') * 10).alias('sepal_length_multiplying'),
#       (pl.col('sepal_length') > 3.0).alias('sepal_length_boolean'),
# ])
# print(df)


df = r_df.groupby('species', maintain_order=True).agg([
      pl.col('sepal_length').mean().alias('sepal_length_mean'),
      pl.col('sepal_length').max().alias('sepal_length_max'),
      pl.col('sepal_length').std().alias('sepal_length_std'),
      pl.col('sepal_width').mean().alias('sepal_width_mean'),
      pl.col('sepal_width').max().alias('sepal_width_max'),
      pl.col('sepal_width').std().alias('sepal_width_std')

])

print(df)