from peewee import CharField, DecimalField
from peewee_setup import BaseModel, db

class User(BaseModel):
    user_id = CharField()
    user_name = CharField()
    profile_pic_url = CharField()
    sentiment_score = DecimalField()
    auth_token = CharField(null=True)

def get_user(user_id):
    return User.get_by_id(user_id)

db.create_tables([User])

