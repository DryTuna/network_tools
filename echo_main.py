from echo_server import server_class
from echo_client import client_class
import pdb
import sys

from multiprocessing import Process, Value

server_socket = server_class()
#client_socket = client_class()

print 'created sockets' + str(type(server_socket))

while True:
    client_socket = client_class()
    message = str(sys.stdin.readline())
    server_process = Process(target = server_socket.server_run,
                               args = (Value,))
    server_process.start()

    client_socket.client_run(message)
    client_socket.client_socket.close()