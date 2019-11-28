from peewee import CharField, DateTimeField, CompositeKey
from peewee_setup import BaseModel, db
import time

# NEED TO CONFIRM IF ALBUM ART URL RETURNED FROM SPOTIFY CAN BE USED BY FRONTEND

NUM_MILLI_PER_DAY = 86400000

class Posts(BaseModel):
    user_id = CharField()
    date_posted = DateTimeField()
    track_id = CharField()

    class Meta:
        primary_key = CompositeKey('user_id', 'time_posted')


db.create_tables([Posts])

def get_post(user_id):
    """
    Returns a post by the user, if it was within the past 24 hours
    """
    try:
        filter_time = int(round(time.time()*1000))-NUM_MILLI_PER_DAY
        post = Posts.get(
            Posts.user_id == user_id, Posts.date_posted > filter_time).execute()
        return post
    # in case of user not found or incorrect parameter user_id
    except:
        return None

def create_post(post_field_mappings):
    """
    Creates a post with the given mappings.
    @param the mappings are a dictionary of fields and their values.
    @return the number of rows created (-1 if error)
    """
    try:
        return Posts.insert(**post_field_mappings).execute()
    # in case of incorrect user field mapping
    except:
        return -1

def delete_current_posts(user_id):
    """
    Deletes the most recent posts by the user. (in the last 24 hours)
    """
    filter_time = int(round(time.time()*1000))-NUM_MILLI_PER_DAY
    return Posts.delete().where(Posts.user_id == user_id, Posts.date_posted > filter_time).execute()
