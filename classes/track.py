from peewee import CharField, FloatField
from playhouse.postgres_ext import JSONField
from peewee_setup import BaseModel, db

# NEED TO CONFIRM IF ALBUM ART URL RETURNED FROM SPOTIFY CAN BE USED BY FRONTEND


class Track(BaseModel):
    track_id = CharField(primary_key=True)
    track_name = CharField()
    artist_name = CharField()
    album_art = JSONField()
    sentiment_score = FloatField(null=True)


db.create_tables([Track])


# Get a tract as dict by
# Args: track_id (string/int of track_id)
# Return: Track as dictionary if found, None if not found
def get_track(track_id):
    try:
        track_array = Track.select().where(
            Track.track_id == track_id).limit(1).dicts().execute()
        return track_array[0]
    # in case of track not found or incorrect parameter track_id
    except:
        return None

# Create a track with provided fields
# Args: track_fields (dictionary- key = field, value = field_value)
# Return: Number of rows created, -1 if error


def create_track(track_field_mappings):
    try:
        return Track.insert(**track_field_mappings).execute()
    # in case of incorrect track field mapping
    except:
        return -1


# Create tracks for each set of provided fields
# Args: array of track_fields (dictionary- key = field, value = field_value)
# Return: Number of rows created, -1 if error
def bulk_create_tracks(track_field_mappings_array):
    try:
        with db.atomic():
            Track.insert_many(track_field_mappings_array).execute()
    except:
        return -1


# Updates track using field_mapping
# Args: track_id (snt of track_id), track_fields (dictionary- key = field, value = field_value)
# Return: Number of rows updated, -1 if error
def update_track(track_id, track_field_mappings):
    try:
        return Track.update(**track_field_mappings).where(Track.track_id == track_id).execute()
    # in case of incorrect track field mapping
    except:
        return -1


# Deletes a track using id
# Args: track_id (int of track_id)
# Return: Number of rows deleted
def delete_track(track_id):
    return Track.delete().where(Track.track_id == track_id).execute()
