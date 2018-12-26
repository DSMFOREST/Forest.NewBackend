import requests

from flask import current_app, Flask
from flask_restful import Api


class Router:

    def __init__(self, app: Flask):
        self.app = app
        self.api = Api(app)

    def register(self):
        from view.auth.login import Login
        self.api.add_resource(Login, '/api/login')

        from view.auth.signUp import SignUp
        self.api.add_resource(SignUp, '/api/sign-up')

        from view.auth.confirm import Confirm
        self.api.add_resource(Confirm, '/confirm/<token>')

        from view.post.post import Post
        self.api.add_resource(Post, '/api/post')

        from view.report.report import Report
        self.api.add_resource(Report, '/api/report')


def send_email(to, link):
    base_text = """
    안녕하세요! 대덕소프트웨어마이스터고등학교 대나무숲 운영진입니다.\n
    본 메일은 귀하의 계정을 확인하기 위한 본인 인증 절차 중 하나이며,\n
    다음 링크에 접속하여 본인 인증을 완료해 주십시오.\n
    본인 확인 링크: {}\n
    대마고 대나무숲 운영진 드림\n
    """
    return requests.post(
        current_app.config['MAIL_API_LINK'],
        auth=(
            "api",
            current_app.config['MAIL_API_AUTH']
        ),
        data={
            "from": "dsm_forest@jaehoon.kim",
            "to": [to],
            "subject": current_app.config['MAIL_SUBJECT'],
            "text": base_text.format(link)
        }
    )
