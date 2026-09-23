from flask import Blueprint, jsonify, request

from src.main.composer.person_creator_composer import person_creator_composer
from src.views.http_types.http_request import HttpRequest

person_routes_bp = Blueprint("person_routes", __name__)


@person_routes_bp.route("/person", methods=["POST"])
def create_person():
    htpp_request = HttpRequest(body=request.json)

    view = person_creator_composer()

    http_response = view.handle(http_request=htpp_request)

    return jsonify(http_response.body), http_response.status_code
