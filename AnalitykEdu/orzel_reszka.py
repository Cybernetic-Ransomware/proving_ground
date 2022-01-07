import random
import time


iterator = 0

while True:
    iterator += 1
    print('Rzucam monetą')
    wynik = random.choice(['O', 'R'])
    wybor = input('Wybierz wynik: [O/R]').upper()

    for i in [3, 2, 1]:
        print(str(i) + '...')
        time.sleep(1)

    if wybor == wynik:
        print(f'Poprawnie! Wygrales za {iterator} razem')
        break

    if iterator == 10:
        print('Dawno nie było tu takiego pechowca. Kończymy na dziś.')
        break

    print('Pudło! Gramy jeszcze raz.')
