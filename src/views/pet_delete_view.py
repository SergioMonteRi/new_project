from src.controllers.interfaces.pet_delete_controller import (
    PetDeleteControllerInterface,
)

from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class PetDeleteView(ViewInterface):
    def __init__(self, controller: PetDeleteControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        if http_request.param is None:
            raise ValueError("Pet id is required")

        pet_id = http_request.param.get("pet_id")

        if pet_id is None:
            raise ValueError("Person id is required")

        self.__controller.delete_pet(pet_id)

        return HttpResponse(status_code=204, body=None)
