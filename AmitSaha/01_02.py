def multi_table(a, b):
    for i in range(1, b+1):
        print(f'{a} x {i} = {a * i:.2f}')


if __name__ == '__main__':
    a = input('Wpisz czynnik: ')
    b = input('Wpisz wielokrotność: ')
    multi_table(float(a), int(b))
