import echo_server

server = Server()
server.server_run()

def test_returnError():
    error_message = echo_server.returnError("There's nothing here.")
    assert error_message[:24] = "HTTP/1.1 400 BAD REQUEST"


def test_bad_URI():
    """This error should be returned because there is no '/' before the hello.html file"""
    client = client_class()
    returnMessage = client.client_run("GET hello.html HTTP/1.1\r\n\r\n")
    assert returnMessage == "HTTP/1.1 <h1> 440 - COOL STORY BRO </h1>"


def test_good_URI():
    client = client_class()
    returnMessage = client.client_run("GET /hello.html HTTP/1.1\r\n\r\n")
    assert returnMessage[len("HTTP/1.1 200 OK")] == "HTTP/1.1 200 OK"


def test_bad_protocol():
    client = client_class()
    returnMessage = client.client_run("GET /hello.html HTT1.1\r\n\r\n")
    assert returnMessage == "HTTP/1.1 <h1> 430 - WRONG PROTOCOL </h1>"


