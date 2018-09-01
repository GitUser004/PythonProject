from socket import *

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("waiting for connecting...")
    tcpCliSock, addr = tcpSerSock.accept()
    print("...connected from:",addr, "enter 'q' to disconnect link")

    while True:
        data = tcpCliSock.recv(BUFSIZE).decode()
        if not data or data == 'q':
            break
        print(">>", "receive:", data)
        tcpCliSock.send(data.encode())
    tcpCliSock.close()
tcpSerSock.close()
