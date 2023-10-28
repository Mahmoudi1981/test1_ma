import socket
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.bind(('127.0.0.1', 5230))
tcpSocket.listen(5)


while True:
    client, addr = tcpSocket.accept()
    print('Received connection from',addr)
    client.send(b'thank you for connecting')
    client.close()
