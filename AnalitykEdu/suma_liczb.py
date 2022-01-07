dane = [1, 3, 5, 2, 11, 7, 18]
indeksy = [x for x in range(0, len(dane))]


# print(dane)
# print(indeksy)

slownik = {}

for x in indeksy:
    slownik.update({dane[x]: [z + dane[x] for z in dane]})
    del slownik[dane[x]][x]

# print(slownik)
result = set()
for x in slownik.keys():
    # print(x, slownik.get(x))

    for y in dane:
        if y in slownik.get(x):
            result.add(f'Suma liczb: {min(x, y - x)} i {max(x, y - x)}, równa: {y} znajduje się z zbiorze wejściowym.')

for x in result:
    print(x)
