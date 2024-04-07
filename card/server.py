import socket
import threading

# Global constants
HOST = 'localhost'  # Change this to your server's IP address if needed
PORT = 12345  # Choose a port number that is not currently in use
MAX_CONNECTIONS = 5

# Game variables
clients = []


def handle_client(client_socket):
    """
    Function to handle communication with a single client.
    """
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break  # If no data is received, close the connection

            # Handle the received data (e.g., process game commands)
            # For simplicity, we'll just print the received data for now
            print(f"Received from client: {data}")

            # Send a response back to the client
            # For now, we'll just echo the received message
            client_socket.sendall(data.encode('utf-8'))
        except ConnectionResetError:
            break

    # Close the client socket when the loop exits
    client_socket.close()


def start_server():
    """
    Function to start the server and listen for incoming connections.
    """
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((HOST, PORT))

    # Listen for incoming connections
    server_socket.listen(MAX_CONNECTIONS)
    print(f"Server is listening on {HOST}:{PORT}")

    try:
        while True:
            # Accept a new connection
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            # Create a new thread to handle communication with the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()

            # Add the client thread to the list of active clients
            clients.append(client_thread)
    except KeyboardInterrupt:
        print("Server shutting down...")
        server_socket.close()

        # Wait for all client threads to terminate
        for client_thread in clients:
            client_thread.join()


if __name__ == "__main__":
    start_server()
