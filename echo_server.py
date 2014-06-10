import socket

def echo_server(num):

    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_IP)

    server_socket.bind((socket.gethostbyname(socket.gethostname()), 50000))
    server_socket.listen(1)
    conn, addr = server_socket.accept()

    print "Client: " + conn.recv(32)

    conn.sendall("Yes, i hear you.")

    num = 1000
