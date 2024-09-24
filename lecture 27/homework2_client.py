import socket
import threading

HOST = '127.0.0.1'
PORT = 65535

nickname = input('Enter Your Nickname: ')

client_socket = socket.socket()
client_socket.connect((HOST, PORT))

def write():
    while True:
        message = f"{nickname} -> {input()}"
        client_socket.send(message.encode('UTF-8'))

def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            client_socket.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
    



