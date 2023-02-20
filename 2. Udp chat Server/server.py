import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
sock.bind(server_address)

print('Chat server is running on {}:{}'.format(*server_address))

clients = []

while True:
    data, address = sock.recvfrom(4096)
    
    print('{}:{} says: {}'.format(*address, data.decode()))

    if address not in clients:
        clients.append(address)
    
    for client_address in clients:
        if client_address != address:
            sock.sendto(data, client_address)
