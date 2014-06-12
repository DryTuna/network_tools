import socket
import os

class server_class():

    def __init__(self):
        self.server_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            socket.IPPROTO_IP)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((socket.gethostbyname(socket.gethostname()), 50000))
        self.server_socket.listen(1)
        self.data_send = ""
        self.keywords=["GET","POST","HEAD",u"PUT",u'DELETE',
                        u"TRACE","OPTIONS","CONNECT","PATCH"]
        self.root_directory = os.getcwd() + '/webroot'

    def server_run(self):
        conn, addr = self.server_socket.accept()
        self.data_send = ""
        while 1:
            data = conn.recv(32)
            if len(data) < 32:
                break
            self.data_send += data
        dataReturn=self.parse_data()
        conn.sendall(dataReturn)
        conn.close()


    def parse_data(self):
        data_decoded=self.data_send.decode('utf-8')
        lines = data_decoded.split("\r\n")
        i = 0
        while i < len(lines):
            lines[i] = lines[i].split(" ")
            i+=1
        method = lines[0][0]
        resource = lines[0][1]
        protocol = lines[0][2]

        print method + resource + protocol

        if method not in self.keywords:
            return self.returnError("KeyWord Error")

        elif resource[0] != "/":
            return self.returnError("Resource Error")

        elif protocol != "HTTP/1.1":
            return self.returnError("Protocol Error")

        elif method == "GET":
            read_file = ""
            with open(self.root_directory + resource, "rb") as the_file:
                read_file = the_file.read()
            if ".html" in resource:
                return self.return_html(read_file)
            elif ".jpg" in resource:
                return self.return_jpg(read_file)
            elif ".png" in resource:
                return self.return_png(read_file)
            else:
                return self.return_200(read_file)
        else:
            return self.return_200('')


    def return_jpg(self, URI):
        return """HTTP/1.1 200 OK\r\nContent-Type:image/jpeg\r
        Content-Length: %i\r\n\r\n%s"""% (len(URI), URI)

    def return_png(self, URI):
        return """HTTP/1.1 200 OK\r\nContent-Type:image/png\r
        Content-Length: %i\r\n\r\n%s"""% (len(URI), URI)

    def return_html(self, URI):
        return 'HTTP/1.1 200 OK\r\nContent-Type: html\r\n\r\n%s'% URI

    def return_200(self, URI):
        return 'HTTP/1.1 200 OK\r\nContent-Type: \r\n\r\n%s'% URI

    def returnError(self, extraInfo):
        return ("HTTP/1.1 400 BAD REQUEST" + extraInfo)


server = server_class()
while True:
    server.server_run()
