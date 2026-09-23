from src.controllers.interfaces.person_finder_controller import (
    PersonFinderControllerInterface,
)

from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class PersonFinderView(ViewInterface):
    def __init__(self, controller: PersonFinderControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        if http_request.param is None:
            raise ValueError("Person id is required")

        person_id = http_request.param.get("person_id")

        if person_id is None:
            raise ValueError("Person id is required")

        response_body = self.__controller.find_person_by_id(person_id)

        return HttpResponse(status_code=200, body=response_body)
