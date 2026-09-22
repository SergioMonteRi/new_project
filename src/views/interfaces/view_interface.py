from abc import ABC, abstractmethod

from src.views.http_types.http_request import HttpResponse
from src.views.http_types.http_response import HttpRequest


class ViewInterface(ABC):
    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass
