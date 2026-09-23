from flask import Blueprint, jsonify

from src.main.composer.pet_delete_composer import pet_delete_composer
from src.main.composer.pet_list_composer import pet_list_composer
from src.views.http_types.http_request import HttpRequest

pet_routes_bp = Blueprint("pets_routes", __name__)


@pet_routes_bp.route("/pets", methods=["GET"])
def list_pets():
    htpp_request = HttpRequest()

    view = pet_list_composer()

    http_response = view.handle(http_request=htpp_request)

    return jsonify(http_response.body), http_response.status_code


@pet_routes_bp.route("/pets/<int:pet_id>", methods=["DELETE"])
def delete_pet_by_id(pet_id: int):
    param = {"pet_id": pet_id}

    htpp_request = HttpRequest(param=param)

    view = pet_delete_composer()

    http_response = view.handle(http_request=htpp_request)

    return jsonify(http_response.body), http_response.status_code
