import echo_server
import echo_client
import pytest
from multiprocessing import Process, Value

def test_echo():
    num = Value('d', 0.0)
    my_socket = echo_server.server_start()
    server_process = Process(target = echo_server.server_run,
                               args = (num, my_socket))
    client_process = Process(target = echo_client.echo_client,
                               args = ("HELLO",))
    server_process.start()
    client_process.start()
    server_process.join()
    client_process.join()

    # connection was made, num changed from 0.0 to 1.0 in server socket
    assert num.value == 1.0