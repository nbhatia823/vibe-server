from peewee import CharField, BigIntegerField, CompositeKey, ForeignKeyField
from peewee_setup import BaseModel, db
from classes.track import Track
from classes.users import Users
from classes.friends import Friends
import time

NUM_MILLI_PER_DAY = 86400000


class UserPosts(BaseModel):
    user_id = ForeignKeyField(Users)
    date_posted = BigIntegerField()  # stored as integer
    track_id = ForeignKeyField(Track)

    class Meta:
        primary_key = CompositeKey('user_id', 'date_posted')


db.create_tables([UserPosts])


def get_all_user_posts(user_id):
    try:
        posts = UserPosts.select(
            UserPosts.date_posted,
            UserPosts.track_id,
            Track.track_name,
            Track.artist_name,
            Track.album_art,
            Track.sentiment_score
        ).join(Track).where(
            UserPosts.user_id == user_id).order_by(UserPosts.date_posted.desc()).dicts().execute()
        posts = [{
            "date_posted": post["date_posted"],
            "track": {
                "track_id": post["track_id"],
                "track_name": post["track_name"],
                "artist_name": post["artist_name"],
                "album_art": post["album_art"],
                "sentiment_score": post["sentiment_score"]
            }
        } for post in posts]
        return posts
    except:
        return None


def get_current_user_posts(user_id):
    """
    Returns a post by the user, if it was within the past 24 hours
    """
    try:
        filter_time = int(round(time.time()*1000))-NUM_MILLI_PER_DAY
        posts = UserPosts.get(
            UserPosts.user_id == user_id,
            UserPosts.date_posted > filter_time).execute()
        return posts
    # in case of user not found or incorrect parameter user_id
    except:
        return None


def create_user_post(post_field_mappings):
    """
    Creates a post with the given mappings.
    @param the mappings are a dictionary of fields and their values.
    @return the number of rows created (-1 if error)
    """
    try:
        return UserPosts.insert(**post_field_mappings).execute()
    # in case of incorrect user field mapping
    except:
        return -1


def delete_current_user_posts(user_id):
    """
    Deletes the most recent posts by the user. (in the last 24 hours)
    """
    filter_time = int(round(time.time()*1000))-NUM_MILLI_PER_DAY
    return UserPosts.delete().where(
        UserPosts.user_id == user_id,
        UserPosts.date_posted > filter_time).execute()


def get_friends_posts(user_id):
    try:
        friends = Friends.select(Friends.friend_id).where(
            Friends.user_id == user_id)
        friend_posts = UserPosts.select(
            UserPosts.user_id,
            Users.user_name,
            Users.profile_pic_url,
            UserPosts.date_posted,
            Track.track_id,
            Track.track_name,
            Track.artist_name,
            Track.album_art,
            Track.sentiment_score
        ).where(
            UserPosts.user_id.in_(friends)
        ).join(Users, on=UserPosts.user_id == Users.user_id
               ).join(Track, on=UserPosts.track_id == Track.track_id
                      ).limit(20).order_by(UserPosts.date_posted.desc()).dicts().execute()
        posts = [{
            "date_posted": post["date_posted"],
            "user": {
                "user_id": post["user_id"],
                "user_name": post["user_name"],
                "profile_pic_url": post["profile_pic_url"],
            },
            "track": {
                "track_id": post["track_id"],
                "track_name": post["track_name"],
                "artist_name": post["artist_name"],
                "album_art": post["album_art"],
                "sentiment_score": post["sentiment_score"]
            }
        } for post in friend_posts]
        return posts
    except:
        return None
