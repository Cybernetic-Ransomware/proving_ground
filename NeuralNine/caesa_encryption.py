# import string
#
#
# def shift_alphabet(alphabets, shift):
#
#     def shifted_alphabet(alphabet, shift):
#         return alphabet[shift:] + alphabet[:shift]
#
#     alphabet = ''.join(alphabets)
#     s_alphabet = ''
#
#     for abc in alphabets:
#         shifted_alphabet(abc, shift).join(s_alphabet)
#
#     return alphabet, s_alphabet
#
#
# def enkryptor(plain_text, shift, alphabets):
#
#     a = shift_alphabet(alphabets, shift)[0]
#     b = shift_alphabet(alphabets, shift)[1]
#
#     table = str.maketrans(a, b)
#
#     return plain_text.translate(table)
#
#
# def dekryptor(encrypted_text, shift, alphabets):
#
#     shift = 26 - shift
#     a = shift_alphabet(alphabets, shift)[0]
#     b = shift_alphabet(alphabets, shift)[1]
#
#     table = str.maketrans(a, b)
#
#     return encrypted_text.translate(table)
#
#
# if __name__ == '__main__':
#     plain_text: str = input('Set message: ')
#     shift: int = int(input('Set shift: ')) % 26
#     alphabets = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]
#
#     print(enkryptor(plain_text, shift, alphabets))
#
#     print(dekryptor(enkryptor(plain_text, shift, alphabets), shift, alphabets))
