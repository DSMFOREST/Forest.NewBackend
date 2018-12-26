from flask import Response
from flasgger import swag_from
from flask_restful import Resource

from docs.auth import CONFIRM_GET
from model.user import UserModel


class Confirm(Resource):

    @swag_from(CONFIRM_GET)
    def get(self, token):

        userId = token.split('.')[0]
        code = token.split('.')[1]

        user = UserModel.objects(userId=userId, token=code).first()

        if not (token or userId or code):
            return Response('인자가 없습니다. 관리자에게 문의하십시오.', 404)

        elif int(code) == user.token:

            UserModel.objects(userId=userId, token=code).update_one(confirmed=True)
            return Response('본인 인증이 완료되었습니다. 로그인 페이지로 다시 이동하십시오.', 201)

        else:
            return Response('올바르지 않은 토큰입니다.', 403)
