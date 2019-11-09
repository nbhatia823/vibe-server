from peewee import CharField, DecimalField
from peewee_setup import BaseModel, db

# NEED TO CONFIRM IF ALBUM ART URL RETURNED FROM SPOTIFY CAN BE USED BY FRONTEND

class Track(BaseModel):
    track_id = CharField()
    track_name = CharField()
    artist_name = CharField()
    album_art_url = CharField()
    sentiment_score = DecimalField()

db.create_tables([Track])