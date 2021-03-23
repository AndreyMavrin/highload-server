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
                       f"Content-Length: {self.content_length}\r\n" + \
                       f"Content-Type: {self.content_type}\r\n\r\n"

    def encode(self):
        if self.body is not None:
            return self.headers.encode() + self.body
        return self.headers.encode()

    def status(self):
        pass


class ResponseOK(Response):
    status = '200 OK'

    def __init__(self, body, path, method):
        super().__init__()

        extension = path.split('.')[len(path.split('.')) - 1]

        if method != 'HEAD':
            self.body = body
        self.content_length = len(body)

        self.content_type = {
            'html': 'text/html',
            'css': 'text/css',
            'js': 'text/javascript',
            'jpg': 'image/jpeg',
            'jpeg': 'image/jpeg',
            'png': 'image/png',
            'gif': 'image/gif',
            'swf': 'application/x-shockwave-flash'
        }.get(extension)
        self.generate_headers()


class ResponseBadResponse(Response):
    status = '400 Bad Response'


class ResponseForbidden(Response):
    status = '403 Forbidden'


class ResponseNotFound(Response):
    status = '404 NotFound'


class ResponseNotAllowed(Response):
    status = '405 NotAllowed'
