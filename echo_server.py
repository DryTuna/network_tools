import socket
import os

class server_class():

    def __init__(self):
        self.server_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            socket.IPPROTO_IP)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #self.server_socket.bind((socket.gethostbyname(socket.gethostname()), 50000))
        self.server_socket.bind(('0.0.0.0', 8000))
        self.server_socket.listen(1)
        self.data_send = ""
        self.keywords=["GET","POST","HEAD",u"PUT",u'DELETE',u"TRACE","OPTIONS","CONNECT","PATCH"]
        self.root_directory = os.getcwd() + '/resources'

    def server_run(self):
        conn, addr = self.server_socket.accept()
        self.data_send = ""
        while 1:
            data = conn.recv(32)
            if len(data) < 32:
                break
            self.data_send += data
        dataReturn=self.parse_data()
        #dataReturn.encode('utf-8')
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
            if ".html" in resource:
                resource = self._read_html(resource)
                return self.return_html(resource)
            elif ".jpg" in resource:
                resource = self._read_jpg(resource)
                return self.return_jpg(resource)
            else:
                return self.return200('')
        else:
            return self.return200('')

    def _read_html(self,resource):
        with open(self.root_directory + resource, "rb") as thefile:
            readFile = thefile.read()
        return readFile

    def _read_jpg(self,resource):
        with open(self.root_directory + resource, "rb") as thefile:
            readFile = thefile.read()
        return readFile

    def return_all(self):
        return_list=['HTTP/1.1']
        return_list.append(messageThing) #for example 200 OK
        return_list.append("Content-Type: " + contentType) #for example text/html
        return_list.append("Content-Length: " + contentLength) #for example len(message)
        return_list.append("\r\n")
        finalMessage = "\r\n".join(return_list)
        return finalMessage


    def return_jpg(self, URI):
        a = 'HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nContent-Length: %i\r\n\r\n%s'% (len(URI), URI)
        return a

    def return_html(self, URI):
        a = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n %s'% URI
        #return a.encode('utf-8')
        return a

    def return200(self, URI="You're good!"):
        a = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n%s'% URI
        #return a.encode('utf-8')
        return a

    def returnError(self, extraInfo):
        errorMessage = ("HTTP/1.1 400 BAD REQUEST" + extraInfo)
        #.encode('utf-8')
        return errorMessage

if __name__ == "__main__":
    server = server_class()
    while True:
        server.server_run()
