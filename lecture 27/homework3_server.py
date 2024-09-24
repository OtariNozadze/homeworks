import socket

HOST = '127.0.0.1'
PORT = 56780

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

clients = set()

def broadcast(message):
    for client in clients:
        server_socket.sendto(message, client)

def receive():
    print("UDP Chat Server is running...")
    while True:
        try:
            message, client_address = server_socket.recvfrom(1024)
            if client_address not in clients:
                clients.add(client_address)
                print(f"Connected With {str(client_address)}")
            broadcast(message)
        except:
            clients.remove(client_address)


receive()

