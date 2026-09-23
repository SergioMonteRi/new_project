from flask import jsonify

from src.exceptions.exception_types.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)


def handle_unprocessable_entity(error: HttpUnprocessableEntityError):
    return jsonify(
        {
            "error": error.name,
            "message": error.message,
            "errors": error.errors,
        }
    ), error.status_code
