import socket

def server_start():
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_IP)

    server_socket.bind((socket.gethostbyname(socket.gethostname()), 50000))
    return server_socket

def server_run(num, server_socket):
    num.value = 1.0
    server_socket.listen(1)
    conn, addr = server_socket.accept()

    line = str(conn.recv(32))
    print "Client: " + line
    conn.sendall(line)
