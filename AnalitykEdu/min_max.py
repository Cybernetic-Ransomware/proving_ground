lista = [1, 4, -4, 7]

# print(min(lista))
# print(max(lista))

najmniejsza = lista[0]
najwieksza = lista[0]

for pozycja in lista:
    if pozycja < najmniejsza:
        najmniejsza = pozycja
    if pozycja > najwieksza:
        najwieksza = pozycja

print(f"Czy {najmniejsza = }? \t {min(lista) == najmniejsza}")
print(f"Czy {najwieksza = }? \t {max(lista) == najwieksza}")
