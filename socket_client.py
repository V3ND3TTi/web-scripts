import socket

# Define server IP and port
SERVER_IP = "127.0.0.1" # Use "localhost" for local testing
PORT = 65432

# Create a TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT)) #Connect to the server

# Send a message
message = "Hello, server!"
client_socket.sendall(message.encode("utf-8"))


# Receive response
response = client_socket.recv(1024).decode("utf-8")
print(f"[Server]: {response}")

client_socket.close()