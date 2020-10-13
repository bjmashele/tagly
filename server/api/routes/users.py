from flask import Blueprint
from flask import request
from flask import url_for, render_template_string
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.users import User, UserSchema
from api.utils.database import db
from flask_jwt_extended import create_access_token

user_routes = Blueprint("user_routes", __name__)


@user_routes.route('/', methods=['POST'])
def create_user():
    try:
        payload = request.get_json()
        payload['password'] = User.generate_hash(payload['password'])
        user_schema = UserSchema()
        user, error = user_schema.load(payload)
        result = user_schema.dump(user.create()).payload
        return response_with(resp.SUCCESS_201)
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@user_routes.route('/login', methods=['POST'])
def authenticate_user():
    try:
        payload = request.get_json()
        current_user = User.find_by_username(payload['username'])
        if not current_user:
            return response_with(resp.SERVER_ERROR_404)
        if User.verify_hash(payload['password'], current_user.password):
            access_token = create_access_token(identity=payload['username'])
            return response_with(resp.SUCCESS_201, value={'message': 'Logged in as {}'.format(current_user.username),
                                                          "access_token": access_token})
        else:
            return response_with(resp.UNAUTHORIZED_401)
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)
