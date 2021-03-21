from tools.request import Request
from constants import const


class MyHandler:
    def handle(self, sock):
        bytes = b''
        while not bytes.endswith(b'\n'):
            bytes += sock.recv(1024)

        data = bytes.decode()
        request = Request(data)

        if request.method not in const.ALLOWED_METHODS:
            return

        if not request.is_ok:
            return
