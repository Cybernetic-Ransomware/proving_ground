import random
import time


total = set(range(1, 50))
winery = set(random.sample(total, 6))


choice = set()
while len(choice) < 6:
    asked = input('Pick a number: ')
    try:
        asked = int(asked)
    except ValueError:
        print('Int value needed')
        continue

    if asked in choice:
        print('You draw this number, pick other one')
        continue

    if not 49 >= asked > 0:
        print('You draw number out of scope <1, 49>, pick other one')
        continue
    choice.add(asked)


points = 0

# for x in choice:
#     if x in winery:
#         points += 1
#
# print(f'Lucky numbers: {winery}')
# print(f'Your choice: {choice}')
# print(f'Your result: {points}')


start = time.time()

while choice != winery:
    points += 1
    winery = set(random.sample(total, 6))

print(f'Count of loteries: {points:,}')
end = time.time()
print(f'Time to process: {(end - start):.2f}s')
