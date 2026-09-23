from pydantic_core import ErrorDetails


class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str, errors: list[ErrorDetails] | None) -> None:
        self.status_code = 422
        self.message = message
        self.errors = errors
        self.name = "UnprocessableEntity"
