import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(1)

print("Server is waiting for connection...")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data: break
    print(f"Client: {data}")
    msg = input("You: ")
    conn.send(msg.encode())

conn.close()
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))

while True:
    msg = input("You: ")
    client_socket.send(msg.encode())
    data = client_socket.recv(1024).decode()
    print(f"Server: {data}")

client_socket.close()
