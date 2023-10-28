import socket
import threading
import getpass

def broadcast_messages(message, exclude_client=None):
    for client_socket in client_sockets:
        if client_socket != exclude_client:
            try:
                message = f"[{username}]: {message}"
                client_socket.send(message.encode())
            except socket.error:
                print("An error occurred while sending the message to a client.")
                client_sockets.remove(client_socket)


def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode()
        except socket.error:
            print(f"Error occurred while receiving message from {client_address}.")
            client_sockets.remove(client_socket)
            break

        if message:
            print(f"Received message: {message}")
            broadcast_messages(message, exclude_client=client_socket)

    client_socket.close()

def main():
    host = '127.0.0.1'  # آدرس IP سرور
    port = 1234  # پورت سرور

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server started. Waiting for clients to connect...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Client {client_address} connected.")

        client_sockets.append(client_socket)

        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

if __name__ == '__main__':
    username = getpass.getuser()  # نام کاربری فعلی که در اجرای کد استفاده شده است.
    client_sockets = []
    main()