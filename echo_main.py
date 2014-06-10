import echo_server
import echo_client
import pdb
import sys

from multiprocessing import Process, Value

<<<<<<< HEAD
def communicate(message):

    #message = str(sys.stdin.readline())
    message = 'hello'

    client_num = 0
    server_num = Value('i', 0)

    server_process = Process(target = echo_server.echo_server, args = (server_num,))
    server_process.start()

    client_num = echo_client.echo_client(message)


    #pdb.set_trace()
    server_process.join()

if __name__ == '__main__':
    communicate('hello')
=======
a = echo_server.server_start()

while True:
    message = str(sys.stdin.readline())
    server_process = Process(target = echo_server.server_run ,args = (a,))
    client_process = Process(target = echo_client.echo_client ,args = (message,))
    server_process.start()
    client_process.start()
    client_process.join()
>>>>>>> e0692016d81784daa8001848af867f2902f658e8
