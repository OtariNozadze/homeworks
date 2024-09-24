import socket

HOST = '127.0.0.1'
PORT = 65435


with socket.socket() as client_socket:
    client_socket.connect((HOST, PORT))

    data = client_socket.recv(1024).decode('UTF-8')
    print(data)