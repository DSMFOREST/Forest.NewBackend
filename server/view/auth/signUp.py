import random

from flask import request, Response, url_for, render_template
from flasgger import swag_from
from flask_restful import Resource

from view import send_email
from view.auth.confirm import Confirm
from docs.auth import SIGN_UP_POST
from model.user import UserModel


class SignUp(Resource):

    @swag_from(SIGN_UP_POST)
    def post(self):
        payload = request.json
        ID = payload['userId']  # 아이디
        EM = payload['email']
        PW = payload['password']

        if UserModel.objects(userId=ID).first():
            return {"status": "The ID already exists."}, 409
        else:
            UserModel(
                userId=ID,
                password=PW,
                name=payload['name'],
                student_number=payload['student_number'],
                email=EM,
                token=int(random.randint(100000, 999999)),
                confirmed=False,
                admin=False
            ).save()

            code = UserModel.objects(userId=ID).first().token

            send_email(
                to=EM,
                link="http://aws.jaehoon.kim:5002/confirm/" + str(ID) + "." + str(code)
            )

        return {"status": "successfully processed!"}, 201
