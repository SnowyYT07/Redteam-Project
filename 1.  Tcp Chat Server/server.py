import socket
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print("Server Started: {}:{}".format(HOST, PORT))


while True:
    client_socket, client_address = server_socket.accept()
    print("Connection from: {}".format(client_address))
    data = client_socket.recv(1024)
    print("message: {}".format(data.decode()))
    client_socket.close()
