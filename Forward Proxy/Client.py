import socket

def start_client(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    print(f"Connected to server {server_ip}:{server_port}")

    try:
        while True:
            message = input("Enter message: ")
            client_socket.sendall(message.encode('utf-8'))
            data = client_socket.recv(1024)
            print(f"Received from server: {data.decode('utf-8')}")
    except KeyboardInterrupt:
        print("Closing connection")
    finally:
        client_socket.close()

if __name__ == "__main__":
    server_ip = '127.0.0.1'
    server_port = 12345
    start_client(server_ip, server_port)
