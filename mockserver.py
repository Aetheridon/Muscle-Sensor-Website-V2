import socket

HOST = "127.0.0.1"   # Localhost
PORT = 5231          # Port to listen on

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to address and port
server.bind((HOST, PORT))

# Start listening
server.listen(1)
print(f"Server listening on {HOST}:{PORT}")

# Accept connection
conn, addr = server.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)  # Receive up to 1024 bytes
    
    if not data:
        break

    message = data.decode()
    print(f"Client says: {message}")

    # Send response back
    response = f"Server received: {message}"
    conn.sendall(response.encode())

conn.close()
server.close()