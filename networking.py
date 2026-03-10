import socket
import struct

def connect(HOST, PORT, latest_data, stop_event):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client.sendto(b"START", (HOST, PORT))
    print("Registered with server, waiting for numbers...")

    while not stop_event.is_set():
        data, addr = client.recvfrom(4096) # 4096b is max, recvfrom will only return the actual size packet
        
        sensorA0, sensorA1 = struct.unpack("<ii", data) # <ii defines how the bytes are structured
        
        latest_data["sensorA0"] = sensorA0
        latest_data["sensorA1"] = sensorA1
        
        print(f"A0: {latest_data["sensorA0"]}, A1: {latest_data["sensorA1"]}")
    
    client.sendto(b"STOP", (HOST, PORT))
    client.close()