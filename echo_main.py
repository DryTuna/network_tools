from echo_server import Server_class
from echo_client import client_class
import pdb
import sys

from multiprocessing import Process, Value

backlog = 5
server_socket = Server_class(backlog)
#client_socket = client_class()
#server_count = Value('i', 1)
processes = {}

#client_socket = client_class()
#message = str(sys.stdin.readline())
for x in range(1, backlog+1):
    processes['server_process{}'.format(x)] = Process(target = server_socket.server_run)

for keys in processes:
    processes[keys].start()
    


#client_socket.client_run(message)
#client_socket.client_socket.close()