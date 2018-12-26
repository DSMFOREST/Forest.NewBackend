from flask import request, abort
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token

from docs.auth import LOGIN_POST
from model.user import UserModel


class Login(Resource):

    @swag_from(LOGIN_POST)
    def post(self):
        payload = request.json
        user_id = payload['userId']
        password = payload['password']

        if UserModel.objects(userId=user_id, password=password):
            return {
                       'access_token': create_access_token(user_id),
                       'refresh_token': create_refresh_token(user_id)
                   }, 201
        else:
            return abort(401)
