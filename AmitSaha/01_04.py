from fractions import Fraction


def sum_frac(a, b):
    print(f'Sum result: {a + b}')


def sub_frac(a, b):
    print(f'Sum result: {a - b}')


def mul_frac(a, b):
    print(f'Sum result: {a * b}')


def div_frac(a, b):
    print(f'Sum result: {a / b}')


def main():
    a = Fraction(input('Set first element: '))
    b = Fraction(input('Set second element: '))
    operation = input('Set type of operation [sum, sub, mul, div]: ')

    op = {'sum': sum_frac, 'sub': sub_frac, 'mul': mul_frac, 'div': div_frac}

    op[operation](a, b)


if __name__ == '__main__':
    main()
