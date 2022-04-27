import time
import winsound


MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',
              ' ': '/',      '.': '',        '\'': '.____.'
              }


def tone_recall(tone: str):
    time.sleep(.3)

    if tone == '.':
        return winsound.Beep(5000, 500)
    elif tone == '-':
        return winsound.Beep(5000, 800)
    elif tone == '/':
        return time.sleep(1.7)
    pass


message = 'This is the end for you my friend i can\'t forgive i won\'t forget.'
message = message.replace('\'', '')         # may be commented out, used to simplify output

message = ' '.join(MORSE_CODE[char] for char in message.upper())

print(message)
for char in message:
    tone_recall(char)

# %%

MORSE_DECODE = {v: k for k, v in MORSE_CODE.items()}
message = ''.join((MORSE_DECODE[char] for char in message.split(' ')))
print(message)
