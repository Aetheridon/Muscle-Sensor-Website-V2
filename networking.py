## Networking code
import socket
import struct

def connect(HOST, PORT):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client.sendto(b"START", (HOST, PORT))
    print("Registered with server, waiting for numbers...")

    while True:
        data, addr = client.recvfrom(4096) # 4096b is max, recvfrom will only return the actual size packet
        value = struct.unpack("i", data)[0]
        print(value)