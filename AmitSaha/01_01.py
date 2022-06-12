
def int_checker(x):
    x = int(x)

    if x % 2 == 0:
        print(f'{x} in even number.')
        print(f'Next even numbers are: {[x for x in range(x + 2 , x + 20, 2)]}')
    else:
        print(f'{x} in odd number.')
        print(f'Next odd numbers are: {[x for x in range(x + 2 , x + 20, 2)]}')

    return None


if __name__ == '__main__':
    x = input('Set a number: ')

    try:
        x = float(x)
        if x.is_integer():
            int_checker(x)
        else:
            print(f'{x} is not an Int type of number')
    except ValueError:
        print(f'{x} is not an instance of Int')
