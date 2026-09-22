from src.controllers.interfaces.pet_list_controller import PetListControllerInterface

from .http_types.http_request import HttpResponse
from .http_types.http_response import HttpRequest
from .interfaces.view_interface import ViewInterface


class PetListView(ViewInterface):
    def __init__(self, controller: PetListControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list_pets()

        return HttpResponse(status_code=200, body=body_response)
