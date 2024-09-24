import socket
import threading

SERVER_IP = '127.0.0.1'
SERVER_PORT = 65535

server_socket = socket.socket()
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()
print(f"Server is listening to port {SERVER_PORT}")

clients = []



def broadcast(message):
    for client in clients:
        client.send(message)
    with open("messages.txt", "a") as txt_file:
        txt_file.write(f"{message.decode()}\n")


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            clients.remove(client)
            client.close()
            break

def receive():
    while True:
        client, address = server_socket.accept()
        print(f"Connected With {str(address)}")
        clients.append(client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()