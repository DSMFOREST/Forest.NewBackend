from flask import redirect
from flask_restful import Resource


class Web(Resource):

    def get(self):

        # return Response(render_template('/index.html'))
        redirect('/docs')
