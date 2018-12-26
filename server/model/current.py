from mongoengine import *


class CurrentModel(Document):

    setting_name = StringField(
        required=True
    )

    data = IntField()
