import sys
import socket

client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_IP
)

client_socket.connect((socket.gethostbyname(socket.gethostname()), 50000))

client_socket.sendall(sys.stdin)

client_socket.shutdown(socket.SHUT_WR)

print client_socket.recv(32)

client_socket.close()