import random


dane = [random.randint(1, 99) for x in range(100)]
dane.sort()

liczba = random.choice(dane)
liczba_iteracji = 0

tabela = dane.copy()


while True:
    middle_index = len(tabela)//2
    wartosc = tabela[middle_index]
    liczba_iteracji += 1

    if liczba == wartosc:
        print(f'Liczba {liczba} została odnaleziona na pozycji {dane.index(liczba)}!')
        print(f'Liczba iteracji: {liczba_iteracji}')
        break
    elif liczba < wartosc:
        tabela = tabela[:middle_index]
        print(middle_index)
    else:
        tabela = tabela[middle_index:]
