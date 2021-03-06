class HTTPError(Exception):
    pass

class HTTP400(HTTPError):
    def __init__(self):
        self.message = "Y U SO BAD"
        self.code = "400"

class HTTP450(HTTPError):
    def __init__(self):
        self.message = "YOU SHALL NOT PASS"
        self.code = "450"

class HTTP430(HTTPError):
    def __init__(self):
        self.message = "WRONG PROTOCOL"
        self.code = "430"

class HTTP440(HTTPError):
    def __init__(self):
        self.message = "NO HOST DETECTED"
        self.code = "440"

class HTTP510(HTTPError):
    def __init__(self):
        self.message = "FILE NOT FOUND"
        self.code = "510"