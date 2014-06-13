from HTTPError import *
import socket
import os
from os.path import isdir
from os.path import isfile
from os import listdir


class server_class():

    def __init__(self):
        self.server_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            socket.IPPROTO_IP)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #self.server_socket.bind((socket.gethostbyname(socket.gethostname()), 50000))
        self.server_socket.bind('0.0.0.0',8000)
        self.keywords=["GET","POST","HEAD","PUT",u"DELETE",
                        "TRACE","OPTIONS","CONNECT","PATCH"]
        self.root_directory = os.getcwd() + '/webroot'
        self.server_socket.listen(1)


    def server_run(self):
        conn, addr = self.server_socket.accept()
        data_send = ""
        while 1:
            data = conn.recv(32)
            if len(data) < 32:
                break
            data_send += data
        response = "HTTP/1.1 " + self.parse_data(data_send)
        print response
        conn.sendall(response)
        conn.close()


    def parse_data(self, r):
        r = r.decode('utf-8')
        lines = r.split("\r\n")
        for i in range(len(lines)):
            lines[i] = lines[i].split(" ")
        try:
            self.check_method(lines[0][0])
            self.check_URI(lines[0][1])
            self.check_protocol(lines[0][2])
            self.check_host(lines[1][0])
        except HTTPError as e:
            return "<h1> {} - {} </h1>".format(e.code, e.message)
        
        pathway = self.root_directory + lines[0][1]
        if isdir(pathway)
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
                html_page.append('<li><a href="{}">{}</a>>/li>'.format(item, item))
            html_page.append("</ul>")
            res = html_page
        
        elif isfile(pathway)
            with open(self.root_directory + lines[0][1], "rb") as the_file:
                res = the_file.read()

            file_type = lines[0][1].split(".")[-1]
            if lines[0][0] == "GET":
                return "200 OK\r\nContent-Type: {}\r\nContent-Length: {}\r\n\r\n{}".format(file_type, len(res), res)

        else:
            raise HTTP510
            

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


server = server_class()
while True:
    server.server_run()
