from tools.request import Request
from constants import const
from tools.response import ResponseOK, ResponseBadResponse, ResponseForbidden, ResponseNotFound,  ResponseNotAllowed
import os
from urllib.parse import unquote


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

        if '/../' in request.path:
            sock.sendall(ResponseForbidden().encode())
            return

        request.path = unquote(request.path.split('?')[0])

        request.path = os.getcwd() + request.path
        if os.path.isdir(request.path):
            request.path += 'index.html'
            if not os.path.isfile(request.path):
                sock.sendall(ResponseForbidden().encode())

        try:
            body = self.read_file(request.path)
        except Exception:
            sock.sendall(ResponseNotFound().encode())
            return

        response = ResponseOK(body, request.path, request.method)
        sock.sendall(response.encode())
