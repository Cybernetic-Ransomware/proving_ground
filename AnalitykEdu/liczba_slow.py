s = 'Ala ma kota'

print(f"Liczba słów: {len(s.split(' '))}")
print(f"Liczba  liter: {len((s.replace(' ', '')))}")
print(f"Liczba unikalnych liter: {len(set(s.lower()))}")

czestotliwosc = {}

for x in s.replace(' ', ''):
    if x not in czestotliwosc.keys():
        czestotliwosc.update({x: 1})
    else:
        czestotliwosc[x] += 1

print(czestotliwosc)
