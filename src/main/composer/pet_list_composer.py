from src.controllers.pet_list_controller import PetListController
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.models.sqlite.settings.connection import db_connection_handler
from src.views.pet_list_view import PetListView


def pet_list_composer():
    model = PetsRepository(db_connection_handler)
    controller = PetListController(model)
    view = PetListView(controller)

    return view
