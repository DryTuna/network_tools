import sys
import socket


def client():
    message = str(sys.stdin)
    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_IP
    )

    #client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #client_socket.bind((socket.gethostbyname(socket.gethostname()), 50000))

    client_socket.connect((socket.gethostbyname(socket.gethostname()), 50000))

    client_socket.sendall(message)

    client_socket.shutdown(socket.SHUT_WR)

    a = client_socket.recv(32)

    client_socket.close()
    print a
    return a

client()
