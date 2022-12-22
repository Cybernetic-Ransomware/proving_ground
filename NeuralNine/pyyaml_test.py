import random
import getpass
import yaml


with open('game_config.yml', 'r') as f:
    config = yaml.safe_load(f)


range_min = config['range']['min']
range_max = config['range']['max']
guesses_allowed = config['guesses']
game_mode = config['mode']


if __name__ == '__main__':

    solved = False

    if game_mode == 'single':
        correct_number = random.randint(range_min, range_max)
    elif game_mode == 'multi':
        correct_number = int(getpass.getpass('Player 2, please input the number to guess: '))
    else:
        print('ConfigurationError, check game_config.yml')
        exit()

    for i in range(guesses_allowed):
        guess = int(input('Enter your guess number: '))

        if guess == correct_number:
            print(f'Correct, you won with {i + 1} tries!')
            solved = True
            break
        elif guess < correct_number:
            print('To low!')
        else:
            print('To high!')

    if not solved:
        print(f'You lost. A correct number was: {correct_number}')
