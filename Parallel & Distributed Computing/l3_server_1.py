import socket
import threading

# List to store connected client sockets along with their IDs
connected_clients = []

def handle_client(client_socket, client_address):
    client_id = len(connected_clients) + 1  # Assigning a unique ID to each client
    print(f"Connection from {client_address}, ID: {client_id}")
    connected_clients.append((client_socket, client_id))  # Add client socket and ID to the list
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received data from {client_address}, ID: {client_id}: {data.decode()}")
        # Prepend client ID to the message
        message_with_id = f"Client {client_id}: {data.decode()}"
        # Broadcast the message to all connected clients except the sender
        for client, _ in connected_clients:
            if client != client_socket:
                client.sendall(message_with_id.encode())
    print(f"Client {client_address}, ID: {client_id} disconnected")
    connected_clients.remove((client_socket, client_id))  # Remove client socket and ID from the list
    client_socket.close()

def start_server():
    host = '127.0.0.1'
    port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
