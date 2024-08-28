import hashlib
import socket

def hash_def(data):
    hash_value = 5381
    for char in data:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
        hash_value &= 0xffffffff
    return hash_value

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is listening on port 12345...")
    
    conn, addr = server_socket.accept()
    print(f"Connection from {addr} has been established.")
    
    data = conn.recv(1024).decode()
    print(f"Received data: {data}")
    
    hash_value = hash_def(data)
    conn.send(str(hash_value).encode())
    
    conn.close()
    server_socket.close()
    
if __name__ == "__main__":
    start_server()