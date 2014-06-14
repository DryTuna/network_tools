import sys
import socket

class client_class():

    def __init__(self):
        self.client_socket = socket.socket(
                    socket.AF_INET,
                    socket.SOCK_STREAM,
                    socket.IPPROTO_IP)
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.client_socket.connect((socket.gethostbyname(socket.gethostname()), 50000))
        

    def client_run(self, message):
        message.encode('utf-8')
        self.client_socket.sendall(message)
        self.client_socket.shutdown(socket.SHUT_WR)
        data_receive = ""
        while 1:
            data = self.client_socket.recv(32)
            data_receive += data
            if len(data) < 32:
                break
        print "Server: " + data_receive.decode('utf-8')
