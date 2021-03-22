class Request:
    def __init__(self, data: str):
        self.data = data

        self.method = None
        self.is_ok = False

        self.headers = {}

        try:
            self.parse_headers()
        except Exception:
            print('Error in parsing')
            return

    def parse_headers(self):
        headers = self.data.split('\r\n')
        if len(headers) == 0:
            return

        self.method, _, _ = headers[0].split()

        for header in headers[1:]:
            if len(header.split(': ')) == 2:
                key, value = header.split(': ')
                self.headers[key] = value

        self.is_ok = True
