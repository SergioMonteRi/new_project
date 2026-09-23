from pydantic import ValidationError

from src.controllers.interfaces.person_creator_controller import (
    PersonCreatorControllerInterface,
)
from src.exceptions.exception_types.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)
from src.schemas.create_person_schema import CreatePersonSchema

from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class PersonCreatorView(ViewInterface):
    def __init__(self, controller: PersonCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        if http_request.body is None:
            raise ValueError("Request body is required")

        try:
            person = CreatePersonSchema.model_validate(http_request.body)
        except ValidationError as e:
            errors = e.errors(include_url=False, include_context=False)

            raise HttpUnprocessableEntityError(
                message="Invalid request body",
                errors=errors,
            ) from e

        response_body = self.__controller.create_person(person_data=person)

        return HttpResponse(status_code=201, body=response_body)
