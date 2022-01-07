import random


word = random.choice(['Kawusia z ciastkiem', 'Słoik z jagodami', 'Pierniczki', 'Herbata z miodem',
                      'Czupakabra w nugacie', 'Słodkie ciągnięte kable']).lower()
word_set = set(word)
allowed_errors = 5

if ' ' in word_set:
    guesses = set(' ')
else:
    guesses = set('')


while True:
    for letter in word:
        if letter in guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print('')

    char = input('Guess next letter of pass the whole word: ').lower()

    if char == word or guesses.issuperset(word_set):
        print(f'Congratulations, you guess the word: {word} and win!')
        break

    if len(char) == 1:
        if char not in word_set:
            allowed_errors -= 1
            print(f'Fail, remaining allowed mistakes: {allowed_errors}!')
        elif char in guesses:
            print('Character already guessed, choose another one.')
        else:
            guesses.add(char)
            if guesses.issuperset(word_set):
                print(f'Congratulations, you guess the word: {word} and win!')
                break

    if allowed_errors == 0:
        print(f'That was your last chance, you can not guess: {word}, but hey! Lets\'s try again')
        break
