from constants import const


class Response:
    def __init__(self):
        self.headers = None
        self.body = None
        self.content_type = None
        self.content_length = 0

        self.generate_headers()

    def generate_headers(self):
        if self.body is not None:
            self.content_length = len(self.body)
        self.headers = f"HTTP/1.1 {self.status}\r\n" + \
                       f"Server: {const.SERVER_NAME}\r\n" + \
                       f"Content-Length: {self.content_length}\r\n"

    def encode(self):
        print(self.headers)
        if self.body is not None:
            return self.headers.encode() + self.body
        return self.headers.encode()

    def status(self):
        pass


class ResponseOK(Response):
    status = '200 OK'


class ResponseForbidden(Response):
    status = '403 Forbidden'


class ResponseNotFound(Response):
    status = '404 NotFound'
