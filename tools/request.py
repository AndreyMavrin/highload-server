class Request:
    def __init__(self, data: str):
        self.data = data

        self.method = None
        self.is_ok = False