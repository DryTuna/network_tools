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
        self.client_socket.sendall(message)
        self.client_socket.shutdown(socket.SHUT_WR)
        data_receive = ""
        while 1:
            data = self.client_socket.recv(32)
            if not data:
                break
            data_receive += data
        print "Server: " + data_receive
