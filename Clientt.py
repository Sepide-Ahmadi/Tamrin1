
import socket

# Set up the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server host and port
server_host = '127.0.0.1'  # Localhost
server_port = 12345        # Port where server is listening

# Connect to the server
client_socket.connect((server_host, server_port))

print("Connected to the server. Type 'exit' to quit the chat.")

# Main chat loop
try:
    while True:
        # Send message to the server
        client_message = input("You: ")
        client_socket.sendall(client_message.encode('utf-8'))
        if client_message.lower() == 'exit':
            print("You disconnected.")
            break

        # Receive server's response
        server_message = client_socket.recv(1024).decode('utf-8')
        print(f"Server: {server_message}")
        if server_message.lower() == 'exit':
            print("Server disconnected.")
            break
except KeyboardInterrupt:
    print("\nClient is shutting down.")
finally:
    client_socket.close()

