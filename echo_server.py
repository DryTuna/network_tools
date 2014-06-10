import socket

class server_class():

    def __init__(self):
        self.server_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            socket.IPPROTO_IP)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((socket.gethostbyname(socket.gethostname()), 50000))
        self.server_socket.listen(1)

    def server_run(self, num):
        num.value = 1.0
        conn, addr = self.server_socket.accept()
        data_send = ""
        while 1:
            data = conn.recv(32)
            if not data:
                break
            data_send += data
        conn.sendall(data_send)
        

