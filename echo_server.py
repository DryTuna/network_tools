import socket

def server_start():
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_IP)

    server_socket.bind((socket.gethostbyname(socket.gethostname()), 50000))
    return server_socket

def server_run(server_socket):
    server_socket.listen(1)
    conn, addr = server_socket.accept()

    print "Client: " + conn.recv(32)

    conn.sendall("Yes, i hear you.")

