import feather
import numpy as np
import pandas as pd


np.random.seed = 42
df_size = 10_000_000


df = pd.DataFrame({
    'a': np.random.rand(df_size),
    'b': np.random.rand(df_size),
    'c': np.random.rand(df_size),
    'd': np.random.rand(df_size),
    'e': np.random.rand(df_size)
})

print(df.head())

# df.to_feather('1M.feather')
feather.write_dataframe(df, '1M.feather')


# df = pd.read_feather('1M.feather')
df = feather.read_dataframe('1M.feather')
print(df.head())


# If you don’t need to change the data on the fly, you should use Feather over CSV.
# 150x faster in saving file; 8x in loading; 2x less space on disc
