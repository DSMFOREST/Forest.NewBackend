from docs import param

LOGIN_POST = {
    'tags': ['Authorization'],
    'parameters': [
        param('userId', "아이디"),
        param('password', "비밀번호")
    ],
    'responses': {
        '201': {
            'description': "JWT 반환 성공",
            "example": {
                "access_token": "dkAhffkDkanxmsJWTzhemdla",
                "refresh_token": "flvmfptlxhzms"
            }
        },
        '401': {
            'description': "없는 ID이거나 비밀번호가 틀렸습니다."
        }
    }
}

SIGN_UP_POST = {
    'tags': ['Authorization'],
    'description': '유저 회원가입',
    'parameters': [
        param('userId', "아이디"),
        param('password', "비밀번호"),
        param('email', '이메일'),
        param('name', '이름'),
        param('student_number', '학번')
    ],
    'responses': {
        '201': {
            'description': "회원가입 성공 / 인증메일 발송 완료"
        },
        '409': {
            'description': "중복된 계정 감지"
        }
    }

}

CONFIRM_GET = {
    'tags': ['Authorization'],
    'description': '이메일을 통한 본인확인',
    'parameters': [
        {
            'name': '링크',
            'description': '/confirm/<userId>.<code>',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': "인증 완료"
        },
        '403': {
            'description': "올바르지 않은 토큰"
        },
        '404': {
            'description': "잘못된 링크"
        }
    }

}
