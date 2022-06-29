
def print_menu():
    print('1. kilometers to miles')
    print('2. miles to kilometers')
    print('3. kilograms to pounds')
    print('4. pounds to kilograms')
    print('5. Celcius degree to Fahrenheit degree')
    print('6. Fahrenheits degree to Celciu degree')


def km_to_miles():
    km = float(input('Set distance in km: '))
    miles = km / 1.609

    print(f'Disntance in miles: {miles:.2f}')


def miles_to_km():
    miles = float(input('Set distance in miles: '))
    km = miles * 1.609

    print(f'Disntance in kilometers: {km:.2f}')


def kg_to_ib():
    kg = float(input('Set mass in kilograms: '))
    ib = kg * 2.2046

    print(f'Mass in pounds: {ib:.2f}')


def ib_to_kg():
    ib = float(input('Set mass in pounds: '))
    kg = ib / 2.2046

    print(f'Mass in kilograms: {kg:.2f}')


def cel_to_fahr():
    cel = float(input('Set temperature in Celcius degrees: '))
    fahr = cel * 9 / 5 + 32

    print(f'Temperature in Fahrenheit degrees: {fahr:.2f}')


def fahr_to_cel():
    fahr = float(input('Set temperature in Fahrenheit degrees: '))
    cel = (fahr - 32) * 5 / 9

    print(f'Temperature in Celcius degrees: {cel:.2f}')


if __name__ == '__main__':
    print_menu()
    choice = int(input('Choose the conventer: '))
    menu_dict = {1: km_to_miles, 2: miles_to_km, 3: kg_to_ib, 4: ib_to_kg, 5: cel_to_fahr, 6: fahr_to_cel}
    menu_dict[choice]()
