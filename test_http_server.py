import echo_server
import echo_client
import time
from multiprocessing import Process, Value



print "begin"
server = echo_server.Server_class(1)
print "server created"
server_process = Process(target = server.server_run)
server_process.start()
#time.sleep(5)
print "running server"


def test_bad_URI():
    """This error should be returned because there is no '/' before the hello.html file"""
    client = echo_client.client_class()
 #   time.sleep(1)
    returnMessage = client.client_run("GET hello.html HTTP/1.1\r\n\r\n")
    assert returnMessage == "HTTP/1.1 400 Y U SO BAD\r\n\r\n<h1> 400 - Y U SO BAD </h1>"


def test_good_URI():
    client = echo_client.client_class()
 #   time.sleep(1)
    returnMessage = client.client_run("GET /sample.txt HTTP/1.1\r\nHost: 127.0.0.1:50000\r\n\r\n")
    assert "very simple text file" in returnMessage


def test_bad_protocol():
    client = echo_client.client_class()
 #   time.sleep(1)
    returnMessage = client.client_run("GET /hello.html HTT1.1\r\n\r\n")
    assert "WRONG PROTOCOL" in returnMessage


def test_injection_attack():
    client = echo_client.client_class()
    returnMessage = client.client_run("GET /../hello.html HTTP/1.1\r\nHost: 127.0.0.1:50000\r\n\r\n")
    assert "FILE NOT FOUND" in returnMessage

def test_image_load():
    client = echo_client.client_class()
    returnMessage = client.client_run("GET /images/sample_1.png HTTP/1.1\r\nHost: 127.0.0.1:50000\r\n\r\n")
    assert "Content-Length: 8760\r\n" in returnMessage
