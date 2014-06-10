import pytest
import echo_server
import echo_client
from multiprocessing import Process
import sys


def test_run():
    #assert echo_client.client_socket != 0
    p1 = Process(target=echo_server.server)
    p1.start()
    p2 = Process(target=echo_client.client)
    p2.start()
    #a = echo_client.client()
    print sys.stdout
