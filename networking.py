## Networking code
import socket
import threading
import time

def connect(HOST, PORT):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client.sendto(b"START", (HOST, PORT))
    print("Registered with server, waiting for numbers...")

    while True:
        data, addr = client.recvfrom(1024)
        print(f"From {addr}: {data.decode().strip()}")