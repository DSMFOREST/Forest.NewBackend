from datetime import datetime
from flask import request, Response
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from docs.report import REPORT_POST
from model.user import UserModel
from model.report import ReportModel
from model.current import CurrentModel


class Report(Resource):

    @swag_from(REPORT_POST)
    @jwt_required
    def post(self):
        userId = get_jwt_identity()
        postId = request.json['postId']
        comment = request.json['comment']

        if UserModel.objects(userId=userId).first():

            count = CurrentModel.objects(setting_name='last_report_id').first().data + 1
            CurrentModel.objects(setting_name='last_report_id').update(data=count)

            ReportModel(
                reportId=count,
                userId=UserModel.objects(userId=userId).first(),
                posted_time=datetime.now(),
                postId=postId,
                content=comment
            ).save()

            return Response('신고 접수 완료됨', 201)

        else:
            return Response('확인되지 않은 계정', 401)
