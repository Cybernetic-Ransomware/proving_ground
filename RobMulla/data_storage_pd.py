import os
from time import time

import pandas as pd
import numpy as np


def get_dataset(size):
    # Create Fake Dataset
    df = pd.DataFrame()
    df['size'] = np.random.choice(['big','medium','small'], size)
    df['age'] = np.random.randint(1, 50, size)
    df['team'] = np.random.choice(['red','blue','yellow','green'], size)
    df['win'] = np.random.choice(['yes','no'], size)
    dates = pd.date_range('2020-01-01', '2022-12-31')
    df['date'] = np.random.choice(dates, size)
    df['prob'] = np.random.uniform(0, 1, size)
    return df

def set_dtypes(df):
    df['size'] = df['size'].astype('category')
    df['team'] = df['team'].astype('category')
    df['age'] = df['age'].astype('int16')
    df['win'] = df['win'].map({'yes':True, 'no': False})
    df['prob'] = df['prob'].astype('float32')
    return df


df = get_dataset(10_000_000)

t1 = time()
df.to_csv('test_csv.csv', index=False)
print(f'CSV without typing: {(time() - t1):.6f} s to write')
t1 = time()
r_data = pd.read_csv('./test_csv.csv')
print(f'CSV without typing: {(time() - t1):.6f} s to read')
print(f"CSV without typing: {(os.path.getsize('./test_csv.csv') / 1024 / 1024):.3f} MB size")
print('---'*10)


df = set_dtypes(df)
t1 = time()
df.to_csv('test_csv.csv', index=False)
print(f'CSV with typing: {(time() - t1):.6f} s to write')
t1 = time()
r_data = pd.read_csv('./test_csv.csv')
print(f'CSV with typing: {(time() - t1):.6f} s to read')
print(f"CSV with typing: {(os.path.getsize('./test_csv.csv') / 1024 / 1024):.3f} MB size")
print('---'*10)


df = set_dtypes(df)
t1 = time()
df.to_pickle('test_pickle.pickle')
print(f'Pickle file: {(time() - t1):.6f} s to write')
t1 = time()
r_data = pd.read_pickle('./test_pickle.pickle')
print(f'Pickle file: {(time() - t1):.6f} s to read')
print(f"Pickle file: {(os.path.getsize('./test_pickle.pickle') / 1024 / 1024):.3f} MB size")
print('---'*10)


df = set_dtypes(df)
t1 = time()
df.to_parquet('test_parquet.parquet')
print(f'Parquet file: {(time() - t1):.6f} s to write')
t1 = time()
r_data = pd.read_parquet('./test_parquet.parquet')
print(f'Parquet file: {(time() - t1):.6f} s to read')
print(f"Parquet file: {(os.path.getsize('./test_parquet.parquet') / 1024 / 1024):.3f} MB size")
print('---'*10)


df = set_dtypes(df)
t1 = time()
df.to_feather('test_feather.feather')
print(f'Feather file: {(time() - t1):.6f} s to write')
t1 = time()
r_data = pd.read_feather('./test_feather.feather')
print(f'Feather file: {(time() - t1):.6f} s to read')
print(f"Feather file: {(os.path.getsize('./test_feather.feather') / 1024 / 1024):.3f} MB size")
print('---'*10)


os.remove('./test_csv.csv')
os.remove('./test_pickle.pickle')
os.remove('./test_parquet.parquet')
os.remove('./test_feather.feather')
