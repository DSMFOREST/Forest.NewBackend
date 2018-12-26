import os

from model.user import UserModel
from model.report import ReportModel
from model.post import PostModel


class ConfigObject(object):
    SWAGGER = {
        'title': 'DSM FOREST',
        'specs_route': '/docs',
        'uiversion': 3,

        'info': {
            'title': 'DSM FOREST API',
            'version': '0.10.0',
            'description': 'DSM FOREST 서비스의 API입니다.'
        },
        'host': 'localhost:5000',
        'basePath': '/',
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'http'  # UserModel, ReportModel, PostModel
        ],
        'tags': [
            {
                'name': 'Authorization',
                'description': '로그인 및 회원가입에 관한 API'
            },
            {
                'name': 'Post',
                'description': '게시글 작성에 관한 API'
            },
            {
                'name': 'Report',
                'description': '부적절한 게시글 신고에 관한 API'
            }
        ]
    }

    JSON_AS_ASCII = False

    JWT_SECRET_KEY = os.getenv('SECRET_KEY', 'INEEDMORETIMETOSTUDY')
    SECRET_KEY = os.getenv('SECRET_KEY', 'INEEDMORETIMETOSTUDY')

    MAIL_SUBJECT = "대덕소프트웨어마이스터고등학교 대나무숲 본인인증 메일입니다."
