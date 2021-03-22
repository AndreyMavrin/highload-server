from tools.request import Request
from constants import const
from tools.response import ResponseOK, ResponseBadResponse, ResponseNotFound,  ResponseNotAllowed
import os


class MyHandler:
    def read_file(self, path):
        with open(path, 'rb') as f:
            body = f.read()
        return body

    def handle(self, sock):
        bytes = b''
        while not bytes.endswith(b'\n'):
            bytes += sock.recv(1024)

        data = bytes.decode()
        request = Request(data)

        if request.method not in const.ALLOWED_METHODS:
            sock.sendall(ResponseNotAllowed().encode())
            return

        if not request.is_ok:
            sock.sendall(ResponseBadResponse().encode())
            return

        request.path = "/home/andrey/highload/highload-server" + request.path
        print(request.path)
        if os.path.isdir(request.path):
            request.path += 'index.html'
            print(request.path)

        try:
            body = self.read_file(request.path)
        except Exception:
            sock.sendall(ResponseNotFound().encode())
            return

        response = ResponseOK(body, request.method)
        print(response.headers)
        print(len(response.body))
        sock.sendall(response.encode())
