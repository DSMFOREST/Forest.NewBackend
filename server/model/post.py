from mongoengine import *

from model.user import UserModel


class PostModel(Document):
    """
    게시글 Collection
    """

    meta = {
        'collection': 'post'
    }

    postId = IntField(
        primary_key=True,
        required=True
    )

    userId = ReferenceField(
        document_type=UserModel,
        required=True
    )

    # 게시된 시간
    posted_time = DateTimeField(
        required=True
    )

    checked = BooleanField(
        required=True
    )

    content = StringField(
        required=True
    )

    # 첨부 이미지 링크
    image = StringField()
