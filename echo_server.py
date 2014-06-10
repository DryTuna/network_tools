import socket

<<<<<<< HEAD
def echo_server(num):

=======
def server_start():
>>>>>>> e0692016d81784daa8001848af867f2902f658e8
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

<<<<<<< HEAD
    conn.sendall("Yes, i hear you.")

    num = 1000
=======
    conn.sendall("Yes, i hear you.")
>>>>>>> e0692016d81784daa8001848af867f2902f658e8
