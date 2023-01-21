import pandas as pd
import numpy as np

from time import sleep
from tqdm import tqdm, trange

chinchilla_color = np.random.choice(['white', 'beige', 'black', 'sapphire', 'violet', 'charcoal', 'velvet'], size=50_000)
chinchilla_weight = np.random.randint(350, 900, size=50_000)

df = pd.DataFrame(data=np.array([chinchilla_color, chinchilla_weight]).T, columns=['color', 'weight'])
print(df.head())


for chinchilla in tqdm(chinchilla_color):
    sleep(0.000001)


for i in range(50):
    sleep(0.1)
print('done without a bar', end='\n\n')

for i in trange(50):
    sleep(0.1)
print('done with a bar')


print(len(chinchilla_color))
for chinchilla in tqdm(chinchilla_color, total=70_000):
    sleep(0.00001)

for chinchilla in tqdm(chinchilla_color, total=len(chinchilla_color)):
    sleep(0.00001)


pbar = tqdm(total=50_000)
for chinchilla in chinchilla_weight:
    pbar.update(1)
    sleep(0.00001)
pbar.close()

total_weight = 0
for weight in tqdm(chinchilla_weight, desc='weight counting', unit=' chinchillas'):
    total_weight += weight
    sleep(0.0001)
#
print(f'{(total_weight/1000):.0f} kilograms')
print(f'{(total_weight/len(chinchilla_weight)):.2f} average weight in grams')


for color in tqdm(chinchilla_color[:18], desc='color_counter', total=18):
    for weight in tqdm(chinchilla_weight[:5], desc='weight_counter', total=5):
        sleep(0.01)


pbar = tqdm(chinchilla_color[:10])
for chinchilla in pbar:
    sleep(0.5)
    pbar.set_description(f'Processing {chinchilla}')


for i in tqdm(range(90_000), ncols=150):
    sleep(0.00001)


for i in tqdm(chinchilla_color, mininterval=2):
    sleep(0.0001)

for i in tqdm(chinchilla_color, maxinterval=100):
    sleep(0.0001)

DEBUG = True
for i in tqdm(chinchilla_color, disable=not DEBUG):
    sleep(0.0001)


tqdm.pandas(desc='Pandas bar')
out = df.progress_apply(lambda row: round(float(row['weight'])/1000, 3), axis=1)
print(out)
#
out = df.groupby('color').progress_apply(lambda row: row['weight'])
print(out)


counter = 0
for chinchilla in tqdm(chinchilla_color):
    if chinchilla == 'beige':
        counter += 1
    if counter == 5_000:
        break
