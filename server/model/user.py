from mongoengine import *


class UserModel(Document):
    """
    사용자 정보 관련 Collection
    """

    meta = {
        'collection': 'user'
    }

    userId = StringField(
        primary_key=True
    )

    password = StringField(
        required=True
    )

    name = StringField(
        required=True
    )

    student_number = StringField(
        required=True
    )

    email = StringField(
        required=True
    )

    token = IntField()

    confirmed = BooleanField(
        required=True
    )

    admin = BooleanField(
        required=True
    )
