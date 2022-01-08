import socket
from colorama import init, Fore


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8000))
server.listen()

client, addr = server.accept()

done = False

while not done:
    msg = (client.recv(1024).decode('utf-8'))

    init(autoreset=True)
    
    if msg == 'quit':
        done = True
    else:
        print(Fore.CYAN + msg)

    client.send(input('Message: ').encode('utf-8'))


client.close()
print('Connection ended')

server.close()
print('Server closed')
