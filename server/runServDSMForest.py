from app import create_app

app = create_app()

"""
    서버 최초 실행 전 주의사항
    : Collection 'CurrentModel'에 각각 다음과 같은 elements 를 'data' = 0으로 초기화할 것
    : setting_name : 'last_report_id', 'last_post_id'
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)