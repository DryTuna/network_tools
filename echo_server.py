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
        #print self.data_send
        dataReturn=self.parse_data()
        #dataReturn.encode('utf-8')
        #print dataReturn
        conn.sendall(dataReturn)
        #conn.sendall()
        conn.close()


    def parse_data(self):
        data_decoded=self.data_send.decode('utf-8')
        lines = data_decoded.split("\r\n")
        i = 0
        while i < len(lines):
            lines[i] = lines[i].split(" ")
            i+=1
        print lines
        method = lines[0][0]
        resource = lines[0][1]
        protocol = lines[0][2]


        print 'parsing data'
        if method not in self.keywords:
            return self.returnError("KeyWord Error")
        elif resource[0] != "/":
            return self.returnError("Resource Error")
        elif protocol != "HTTP/1.1":
            return self.returnError("Protocol Error")
        elif method == "GET":
            resource = self._read_resource(resource)
            return self.return200(resource)
        else:
            return self.return200('')

    def _read_resource(self,resource):
        cwd = os.getcwd()
        thefile = open(cwd + '/resources' + resource, "rb")
        readFile = thefile.read()
        print readFile
        return readFile

    def return200(self, URI="You're good!"):
        a = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n <b>%s</b>'% URI
        return a.encode('utf-8')

    def returnError(self, extraInfo):
        errorMessage = ("HTTP/1.1 400 BAD REQUEST" + extraInfo).encode('utf-8')
        return errorMessage


server = server_class()
while True:
    server.server_run()
