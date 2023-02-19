import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
def receive_messages():
    while True:
        data, _ = sock.recvfrom(4096)
        print(data.decode())
threading.Thread(target=receive_messages, daemon=True).start()

name = input('Enter your name: ')

while True:

    message = input('> ')
    data = '{}: {}'.format(name, message).encode()
    sock.sendto(data, server_address)
