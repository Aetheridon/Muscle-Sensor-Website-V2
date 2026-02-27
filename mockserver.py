import socket
import random
import time

HOST, PORT = "127.0.0.1", 8888

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))  

print(f"UDP server listening on {HOST}:{PORT}")

data, addr = server.recvfrom(1024) # client sends a single packet so we can learn its address
print(f"Client registered from {addr}: {data.decode()}")

try:
    while True:
        n = random.randint(0, 1_000_000)
        server.sendto(f"{n}\n".encode(), addr)
        time.sleep(.2) # throttle
except KeyboardInterrupt:
    print("\nServer stopped")
finally:
    server.close()