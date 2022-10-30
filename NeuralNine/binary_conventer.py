message = ' Gotta knock a little harder \n Break through the door'
binary = ' '.join(format(ord(char), 'b') for char in message)
decoded = ''.join(chr(int(char, 2)) for char in binary.split(' '))


print(message)
print('---' * 10)
print(binary)
print('---' * 10)
print(decoded)
