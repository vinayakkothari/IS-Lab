import hashlib
import socket

def hash_def(data):
    hash_value = 5381
    for char in data:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
        hash_value &= 0xffffffff
    return hash_value

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    
    # data = input("Enter data:  ")
    data = "sample data"
    client_socket.send(data.encode())
    
    received_hash = int(client_socket.recv(1024).decode())
    local_hash = hash_def(data)
    
    if received_hash == local_hash:
        print("Data integrity verified. No corruption detected.")
    else:
        print("Warning! Data corruption detected.")
        
    client_socket.close()
    
if __name__ == "__main__":
    start_client()