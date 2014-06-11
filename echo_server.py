import socket

class server_class():

    def __init__(self):
        self.server_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            socket.IPPROTO_IP)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((socket.gethostbyname(socket.gethostname()), 50000))
        #self.server_socket.bind(('127.0.0.1', 50000))
        self.server_socket.listen(1)
        self.data_send = ""
        self.keywords=["GET","POST","HEAD",u"PUT",u'DELETE',u"TRACE","OPTIONS","CONNECT","PATCH"]

    def server_run(self):
#        num.value = 1.0
#NOT SURE ABOUT THIS LOOP 
        conn, addr = self.server_socket.accept()
        self.data_send = ""
        while 1:
            data = conn.recv(32)
            if len(data) < 32:
                break
            self.data_send += data
        print 'sending data'
        dataReturn=self.parse_data()
        dataReturn.encode('utf-8')
        conn.sendall('AHHHHHHH')
        #conn.sendall('HTTP/1.1 200 OK\r\n\r\n')
        conn.close()


    def parse_data(self):
        data_decoded=self.data_send.decode('utf-8')
        lines = data_decoded.split("\r\n")
        i = 0
        while i < len(lines):
            lines[i] = lines[i].split(" ")
            i+=1

        print 'parsing data'
        if lines[0][0] not in self.keywords:
            return self.returnError("KeyWord Error")
        elif lines[0][1][0] != "/":
            return self.returnError("Resource Error")
        elif lines[0][2] != "HTTP/1.1":
            return self.returnError("Protocol Error")
        elif lines[0][0] == "GET":
            return self.return200(lines[0][1])
        else:
            return self.return200('')

    def return200(self, URI):
        a = "HTTP/1.1 200 OK"
        if not URI:
            return a.encode('utf-8')
        a += "\r\n" + URI
        return a.encode('utf-8')

    def returnError(self, extraInfo):
        errorMessage = ("HTTP/1.1 400 BAD REQUEST" + extraInfo).encode('utf-8')
        return errorMessage


server = server_class()
server.server_run()
