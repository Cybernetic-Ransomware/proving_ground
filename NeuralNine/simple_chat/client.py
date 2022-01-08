import socket
from colorama import init, Fore


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8000))


done = False

while not done:
    client.send(input('Message: ').encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')

    init(autoreset=True)

    if msg == 'quit':
        done = True
    else:
        print(Fore.MAGENTA + msg)


client.close()
print('Connection ended')
