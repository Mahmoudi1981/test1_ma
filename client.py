import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            process_message(message)
        except socket.error:
            print("An error occurred while receiving the message.")
            client_socket.close()
            break

def process_message(message):
    if message:
        sender_index = message.index(":")
        sender = message[1:sender_index]
        print(f"{sender}: {message[sender_index+2:]}")

def send_message(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode())

def main():
    host = '127.0.0.1'  # آدرس IP سرور
    port = 1234  # پورت سرور

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
    except socket.error:
        print("Unable to connect to the server.")
        return

    print("Connected to server.")
    username = input("Enter your username: ")

    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    threading.Thread(target=send_message, args=(client_socket,)).start()

if __name__ == '__main__':
    main()