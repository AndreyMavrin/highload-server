from constants import const
from server.handler import MyHandler

import socket
import os
import logging


class Server:
    def __init__(self, handler: MyHandler):
        self.handler = handler

        self.socket = None
        self.workers = []

        self.host = const.ADDRESS
        self.port = const.PORT
        self.max_connections = const.MAX_CONNECTIONS
        self.thread_limit = const.THREAD_LIMIT

    def prepare_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(self.max_connections)
        print('Starting listen socket')

    def run(self):
        self.prepare_socket()
        for i in range(self.thread_limit):
            pid = os.fork()

            if pid == 0:
                print('Starting fork: ' + str(i))
                while True:
                    conn, address = self.socket.accept()

                    try:
                        self.handler.handle(conn)
                    except Exception:
                        logging.error('Error in connection')

                    conn.close()
                    print('connection closed ' + str(address[1]))
            else:
                self.workers.append(pid)

        for worker in self.workers:
            os.waitpid(worker, 0)
