from flask import Blueprint, jsonify

from src.main.composer.pet_list_composer import pet_list_composer
from src.views.http_types.http_request import HttpRequest

pet_routes_bp = Blueprint("pets_routes", __name__)


@pet_routes_bp.route("/pets", methods=["GET"])
def list_pets():
    htpp_request = HttpRequest()

    view = pet_list_composer()

    http_response = view.handle(http_request=htpp_request)

    return jsonify(http_response.body), http_response.status_code
