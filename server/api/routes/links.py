from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.links import Link, LinkSchema
from api.utils.database import db
# from flask_jwt_extended import (jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

link_routes = Blueprint("link_routes", __name__)


@link_routes.route('/', methods=['POST'])
# @jwt_required
def create_link():
    try:
        payload = request.get_json()
        link_schema = LinkSchema()
        link, error = link_schema.load(payload)
        result = link_schema.dump(link.create())
        return response_with(resp.SUCCESS_201, value={"link": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@link_routes.route('/', methods=['GET'])
def get_link_list():
    fetched = Link.query.all()
    link_schema = LinkSchema(many=True, only=['user_id','title', 'url_string'])
    links, error = link_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"links": links})



@link_routes.route('/<int:id>', methods=['PUT'])
# @jwt_required
def update_link_detail(id):
    payload = request.get_json()
    get_link = Link.query.get_or_404(id)
    get_link.title = payload['title']
    get_link.url_string = payload['url_string']
    get_link.summary = payload['summary']
    db.session.add(get_link)
    db.session.commit()
    link_schema = LinkSchema()
    link, error = link_schema.dump(get_link)
    return response_with(resp.SUCCESS_200, value={"link": link})


@link_routes.route('/<int:id>', methods=['DELETE'])
# @jwt_required
def delete_link(id):
    get_link = Link.query.get_or_404(id)
    db.session.delete(get_link)
    db.session.commit()
    return response_with(resp.SUCCESS_204)
