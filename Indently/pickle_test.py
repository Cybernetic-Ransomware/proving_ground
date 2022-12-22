import pickle
import json
from fractions import Fraction

from pdfminer.utils import pick


class Frut:
    def __init__(self, name: str, calories: int):
        self.name = name
        self.calories = calories

    def describe_fruit(self):
        print(self.name, self.calories, sep=': ')


if __name__ == '__main__':
    f_01: Frut = Frut('apple', 58)
    f_01.describe_fruit()

    # with open('f_01.json', 'w') as file:
    #     data = {'name': f_01.name,
    #             'calories': f_01.calories}
    #
    #     json.dump(data, file)
    #
    # f_01.calories = 88
    # f_01.describe_fruit()
    #
    # with open('f_01.json', 'r') as file:
    #     data = json.load(file)
    #     print(data)

    with open('f_01.pickle', 'wb') as file:
        pickle.dump(f_01, file)

    with open('f_01.pickle', 'rb') as file:
        f_02: Frut = pickle.load(file)

    f_01.calories = 88
    f_01.describe_fruit()
    f_02.describe_fruit()
