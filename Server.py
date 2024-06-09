import socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Listen for up to 5 connections
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        handle_client(client_socket)

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received data: {data.decode('utf-8')}")
        client_socket.sendall(data)  # Echo back the data to the client

    client_socket.close()

if __name__ == "__main__":
    host = '0.0.0.0'  # Listen on all interfaces
    port = 12345
    start_server(host, port)
