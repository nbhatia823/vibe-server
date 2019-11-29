
from peewee import CharField, BigIntegerField, CompositeKey, ForeignKeyField
from peewee_setup import BaseModel, db
from classes.users import Users
import time

# NEED TO CONFIRM IF ALBUM ART URL RETURNED FROM SPOTIFY CAN BE USED BY FRONTEND

NUM_MILLI_PER_DAY = 86400000


class Friends(BaseModel):
    user_id = ForeignKeyField(Users)
    friend_id = ForeignKeyField(Users)

    class Meta:
        primary_key = CompositeKey('user_id', 'friend_id')


db.create_tables([Friends])

# CREATES friend relationship both ways


def get_friends(user_id):
    try:
        friends = Friends.select(
            Users.user_id,
            Users.user_name,
            Users.profile_pic_url
        ).join(Users, on=Friends.friend_id).where(Friends.user_id == user_id).dicts().execute()
        friends = [friend for friend in friends]
        return friends
    except:
        return None


def add_friend(user_id, friend_id):
    try:
        Friends.insert(
            {"user_id": user_id,
             "friend_id": friend_id}).execute()
        Friends.insert(
            {"user_id": friend_id,
             "friend_id": user_id}).execute()
        return True
    except:
        return False


def delete_friend(user_id, friend_id):
    try:
        Friends.delete().where(
            Friends.user_id == user_id,
            Friends.friend_id == friend_id).execute()
        Friends.delete().where(
            Friends.user_id == friend_id,
            Friends.friend_id == user_id).execute()
        return True
    except:
        return False
