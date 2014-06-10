import echo_server
import echo_client
import pdb
import sys

from multiprocessing import Process, Value

a = echo_server.server_start()

while True:
    message = str(sys.stdin.readline())
    server_process = Process(target = echo_server.server_run,
                               args = (Value, a,))
    client_process = Process(target = echo_client.echo_client,
                               args = (message,))
    server_process.start()
    client_process.start()
    client_process.join()
