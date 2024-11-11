import socket

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the server to a specific address and port
server_host = '127.0.0.1'  # Localhost
server_port = 12345        # Port to listen on
server_socket.bind((server_host, server_port))

# Start listening for incoming connections (max 5 clients in queue)
server_socket.listen(1)

print(f"Server is listening on {server_host}:{server_port}...")

# Accept a connection from the client
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

# Main chat loop
try:
    while True:
        # Receive message from the client
        client_message = client_socket.recv(1024).decode('utf-8')
        if client_message.lower() == 'exit':
            print("Client disconnected.")
            break
        print(f"Client: {client_message}")

        # Send message to the client
        server_message = input("You: ")
        client_socket.sendall(server_message.encode('utf-8'))
        if server_message.lower() == 'exit':
            print("You disconnected.")
            break
except KeyboardInterrupt:
    print("\nServer is shutting down.")
finally:
    client_socket.close()
    server_socket.close()
