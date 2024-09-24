import socket
import threading

UDP_IP = '127.0.0.1'
UDP_PORT = 56780

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

nickname = input("Enter Nickname: ")
def write():
    while True:
        print("hello")
        message = f"{nickname} -> {input()}"
        client_socket.sendto(message.encode(), (UDP_IP, UDP_PORT))
    
def receive():
    while True:
        try:
            message, _ = client_socket.recvfrom(1024)
            print(message.decode())
        except Exception as e:
            client_socket.close()
            break


write_thread = threading.Thread(target=write)
write_thread.start()

receive_thread = threading.Thread(target=receive)
receive_thread.start()


