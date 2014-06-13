import echo_server
import echo_client
import time
from multiprocessing import Process, Value



print "begin"
server = echo_server.Server_class()
print "server created"
server_process = Process(target = server.server_run)
server_process.start()
#time.sleep(5)
print "running server"


def test_returnError():
    print "started first test"
    error_message = echo_server.returnError("There's nothing here.")
    assert error_message[:24] == "HTTP/1.1 400 BAD REQUEST"


def test_bad_URI():
    """This error should be returned because there is no '/' before the hello.html file"""
    client = echo_client.client_class()
 #   time.sleep(1)
    returnMessage = client.client_run("GET hello.html HTTP/1.1\r\n\r\n")
    assert returnMessage == "HTTP/1.1 <h1> 440 - COOL STORY BRO </h1>"


def test_good_URI():
    client = echo_client.client_class()
 #   time.sleep(1)
    returnMessage = client.client_run("GET /hello.html HTTP/1.1\r\n\r\n")
    assert returnMessage[len("HTTP/1.1 200 OK")] == "HTTP/1.1 200 OK"


def test_bad_protocol():
    client = echo_client.client_class()
 #   time.sleep(1)
    returnMessage = client.client_run("GET /hello.html HTT1.1\r\n\r\n")
    assert returnMessage == "HTTP/1.1 <h1> 430 - WRONG PROTOCOL </h1>"


def test_injection_attack():
    client = echo_client.client_class()
    returnMessage = client.client_run("GET /../hello.html HTT1.1\r\n\r\n")
    assert returnMessage == "HTTP/1.1 <h1> 510 - FILE NOT FOUND </h1>"


