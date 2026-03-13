import socket
import struct

def verify_server(HOST, PORT):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(3)

    try:
        client.sendto(b"ONLINE", (HOST, PORT))
        print("sent verification request to server")

        data, addr = client.recvfrom(4096)

        if data == b"ACK" and addr == (HOST, PORT):
            return True
        
        return False

    except socket.timeout:
        return False
    
    finally:
        client.close()

def connect(HOST, PORT, latest_data, stop_event):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client.sendto(b"START", (HOST, PORT))
    print("Registered with server, waiting for numbers...")

    while not stop_event.is_set():
        data, addr = client.recvfrom(4096) # 4096b is max, recvfrom will only return the actual size packet
        
        sensorA0, sensorA1 = struct.unpack("<ff", data) # <ii defines how the bytes are structured

        latest_data["sensorA0"] = sensorA0
        latest_data["sensorA1"] = sensorA1
        
        print(f"A0: {latest_data["sensorA0"]:.3f}, A1: {latest_data["sensorA1"]:.3f}")
    
    client.sendto(b"STOP", (HOST, PORT))
    client.close()