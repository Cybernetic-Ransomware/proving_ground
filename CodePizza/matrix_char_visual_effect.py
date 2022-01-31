import random
import os
import time


def main():

    frequency: int = 100
    columns: int = 240
    colors: str = '03'
    delay: float = 0.04

    allowed_chars = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    allowed_chars.extend(f'{" _" * frequency}'.split(sep='_'))

    os.system(f"mode con cols={columns} lines=80")
    os.system(f"color {colors}")

    while True:
        for i in range(columns):
            print(random.choice(allowed_chars), sep='', end='')
        print()
        time.sleep(delay)


if __name__ == '__main__':
    main()
