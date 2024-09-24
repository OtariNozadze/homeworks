
import socket

HOST = '0.0.0.0'
PORT = 65435


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))

    server_socket.listen()
    connection_socket, client_address = server_socket.accept()
    print(f"Client Connected From: {client_address}")
    connection_socket.send("Connection was successful!".encode())

