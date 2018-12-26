from datetime import datetime
from flask import request, Response
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from docs.post import POST_POST
from model.current import CurrentModel
from model.user import UserModel
from model.post import PostModel


class Post(Resource):

    @swag_from()
    def get(self):

        pass

    @swag_from(POST_POST)
    @jwt_required
    def post(self):
        payload = request.json
        content = payload['content']
        userId = get_jwt_identity()

        if content and userId and UserModel.objects(userId=userId).first():

            count = CurrentModel.objects(setting_name='last_post_id').first().data + 1
            CurrentModel.objects(setting_name='last_post_id').update(data=count)

            PostModel(
                postId=count,
                userId=UserModel.objects(userId=userId).first(),
                posted_time=datetime.now(),
                checked=False,
                content=content
            ).save()

            return Response('게시글 업로드 성공', 201)
        else:
            return Response('인증 실패', 401)
