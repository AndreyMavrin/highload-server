from server import server
from server.handler import MyHandler

if __name__ == '__main__':
    server = server.Server(handler=MyHandler())
    server.run()