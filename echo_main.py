import echo_server
import echo_client
import pdb
import sys

from multiprocessing import Process

message = str(sys.stdin.readline())

server_process = Process(target = echo_server.echo_server)
client_process = Process(target = echo_client.echo_client, args=(message,))
server_process.start()
client_process.start()
#pdb.set_trace()
server_process.join()
client_process.join()