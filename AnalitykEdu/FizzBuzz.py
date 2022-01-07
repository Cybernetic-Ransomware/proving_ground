dane = [x for x in range(1, 101)]
wynik = []


for x in dane:
    if x % 3 == 0 and x % 5 == 0:
        wynik.append('FizzBuzz')
    elif x % 3 == 0:
        wynik.append('Fizz')
    elif x % 5 == 0:
        wynik.append('Buzz')
    else:
        wynik.append(x)

print(wynik)
print(len(wynik))
