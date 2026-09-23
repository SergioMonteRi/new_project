class HttpNotFoundError(Exception):
    def __init__(self, message: str) -> None:
        self.status_code = 404
        self.message = message
        self.name = "NotFound"
