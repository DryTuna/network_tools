from HTTPError import *
import socket
import os
from os.path import isdir
from os.path import isfile
from os import listdir
import mimetypes


class Server_class():

    def __init__(self, backlog):
        self.server_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            socket.IPPROTO_IP)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #print socket.gethostbyname(socket.gethostname())
        #self.server_socket.bind(('0.0.0.0',8000))

        self.server_socket.bind((socket.gethostbyname(socket.gethostname()), 8000))
        #self.server_socket.bind(("127.0.0.1", 50000))
        self.keywords=["GET","POST","HEAD","PUT",u"DELETE",
                        "TRACE","OPTIONS","CONNECT","PATCH"]
        self.root_directory = os.getcwd() + '/webroot'
        self.server_socket.listen(backlog)


    def server_run(self):
        while True:
            conn, addr = self.server_socket.accept()
            data_send = ""
            while 1:
                data = conn.recv(32)
                data_send += data
                if len(data) < 32:
                    break
            print data_send
            response = "HTTP/1.1 " + self.parse_data(data_send)
            conn.sendall(response)
            conn.close()

    def parse_data(self, r):
        r = r.decode('utf-8')
        lines = r.split("\r\n")
        for i in range(len(lines)):
            lines[i] = lines[i].split(" ")
        pathway = self.root_directory + lines[0][1]
        print lines
        try:
            self.check_method(lines[0][0])
            self.check_URI(lines[0][1])
            self.check_protocol(lines[0][2])
            self.check_host(lines[1][0])
            self.check_exists(lines[0][1])
        except HTTPError as e:
            return "{} {}\r\n\r\n".format(e.code, e.message) + "<h1> {} - {} </h1>".format(e.code, e.message)

        res = ""
        file_type = "text/html"

        if isdir(pathway):
            html_page = ["<p>Directories and Files "]
            html_page.append(lines[0][1])
            html_page.append("</p><ul>")
            directories = []
            files = []
            for item in listdir(pathway):
                if isfile(pathway+item):
                    files.append(item)
                else:
                    directories.append(item + '/')
            dirs_files = directories + files
            for item in dirs_files:
                html_page.append('<li><a href="{}">{}</a></li>'.format(item, item))
            html_page.append("</ul>")
            res = '.'.join(html_page)

        elif isfile(pathway):
            with open(self.root_directory + lines[0][1], "rb") as the_file:
                res = the_file.read()

            #file_type = lines[0][1].split(".")[-1]
            file_type = mimetypes.guess_type(pathway)
            print file_type

        if lines[0][0] == "GET":
            return "200 OK\r\nContent-Type: {}\r\nContent-Length: {}\r\n\r\n{}".format(file_type, len(res), res)
        return ""


    def check_method(self, x):
        if x not in self.keywords:
            raise HTTP450
    def check_URI(self, x):
        if x[0] != "/":
            raise HTTP400
    def check_protocol(self, x):
        if x != "HTTP/1.1":
            raise HTTP430
    def check_host(self, x):
        if "Host" not in x:
            raise HTTP440
    def check_exists(self,x):
        pathway = self.root_directory + x
        if (not isdir(pathway)) and (not isfile(pathway)) or ('..' in pathway):
            raise HTTP510



if __name__ == '__main__':
    server = Server_class(1)
    server.server_run()
