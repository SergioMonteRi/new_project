from flask import Blueprint, jsonify, request

from src.main.composer.person_creator_composer import person_creator_composer
from src.main.composer.person_finder_composer import person_finder_composer
from src.views.http_types.http_request import HttpRequest

person_routes_bp = Blueprint("person_routes", __name__)


@person_routes_bp.route("/person", methods=["POST"])
def create_person():
    htpp_request = HttpRequest(body=request.json)

    view = person_creator_composer()

    http_response = view.handle(http_request=htpp_request)

    return jsonify(http_response.body), http_response.status_code


@person_routes_bp.route("/person/<int:person_id>", methods=["GET"])
def find_person_by_id(person_id: int):
    param = {"person_id": person_id}

    htpp_request = HttpRequest(param=param)

    view = person_finder_composer()

    http_response = view.handle(http_request=htpp_request)

    return jsonify(http_response.body), http_response.status_code
