import string


def enkryptor_ASCII(plain_text, shift):

    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]

    table = str.maketrans(alphabet, shifted)

    return plain_text.translate(table)


def dekryptor_ASCII(encrypted_text, shift):

    alphabet = string.ascii_lowercase
    reshifted = alphabet[26-shift:] + alphabet[:26-shift]

    table = str.maketrans(alphabet, reshifted)

    return encrypted_text.translate(table)


if __name__ == '__main__':
    plain_text = input('Set message: ').lower()
    shift = int(input('Set shift: ')) % 26

    print(enkryptor_ASCII(plain_text, shift))

    print(dekryptor_ASCII(enkryptor_ASCII(plain_text, shift), shift))
