## Networking code
import socket

def connect(HOST, PORT):
    # Create socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    print("Connected!")
    client.connect((HOST, PORT))

    while True:
        message = input("Send to server: ")
        
        if message.lower() == "exit":
            break

        client.sendall(message.encode())

        data = client.recv(1024)
        print("Server replied:", data.decode())

    return 0