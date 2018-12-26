from . import param, jwt_header

POST_POST = {
    'tags': ['Post'],
    'parameters': [jwt_header, param('content', '내용')],
    'responses': {
        '201': {
            'description': "게시글 업로드 성공"
        },
        '401': {
            'description': "인증 실패"
        }
    }
}