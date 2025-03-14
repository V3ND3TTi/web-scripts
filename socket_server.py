import socket

# Define server settings
HOST = "0.0.0.0"    # Listen on all available network interfaces
PORT = 65432        # Port number (must be > 1024 if not running as root)

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT)) # Bind socket to IP and Port
server_socket.listen(1) # Listen for incoming connections (1 client at a time)

print(f"[*] Listening on {HOST}:{PORT}...")

while True:
    client_socket, client_address = server_socket.accept() #Accept connections
    print(f"[+] Connection from {client_address}")
    
    # Receive message from client
    message = client_socket.recv(1024).decode("utf-8")
    print(f"[Client]: {message}")
    
    # Send response
    response = "Hello from server!"
    client_socket.sendall(response.encode("utf-8"))
    
    client_socket.close() # Close connection