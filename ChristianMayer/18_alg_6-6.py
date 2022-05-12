"""
Cesar code
    basic, with very strict input
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
to_decode = 'kebfwnavrkanqpubqmn'

rt13 = lambda x: ''.join(alphabet[(alphabet.find(char) + 13) % 26] for char in x.lower())


print(rt13(to_decode))
