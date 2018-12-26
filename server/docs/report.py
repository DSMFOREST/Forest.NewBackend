from . import param, jwt_header

REPORT_POST = {
    'tags': ['Report'],
    'parameters': [jwt_header, param('postId', '게시글 고유번호', type='int'), param('comment', '신고 내용')],
    'responses': {
        '201': {
            'description': "신고 접수 완료됨"
        },
        '401': {
            'description': "확인되지 않은 계정"
        }
    }
}
