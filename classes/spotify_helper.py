
import requests
from config import Config

"""
Helper class for all Spotify API queries

references:
https://developer.spotify.com/documentation/general/guides/authorization-guide/#authorization-code-flow
"""


class SpotifyHelper:

    @staticmethod
    def search_spotify(query):
        query.replace(" ", "%20")
        url = f'{Config.SPOTIFY_API_URL}/v1/search?q={query}&type=track&limit=4'
        resp = requests.get(url, headers=Config.SPOTIFY_REQ_HEADERS)
        return resp.json()["tracks"]

    @staticmethod
    def get_track_sentiment_score(track_id):
        url = f'{Config.SPOTIFY_API_URL}/v1/audio-features/' + str(track_id)
        resp = requests.get(url, headers=Config.SPOTIFY_REQ_HEADERS)
        if resp.status_code == 400:
            return None
        else:
            return float(resp.json()["valence"])

    @staticmethod
    def get_track_by_id(track_id):
        url = f'{Config.SPOTIFY_API_URL}/v1/tracks/' + str(track_id)
        resp = requests.get(url, headers=Config.SPOTIFY_REQ_HEADERS)
        if resp.status_code == 400:
            return None
        else:
            resp_json = resp.json()
            sentiment_score = SpotifyHelper.get_track_sentiment_score(track_id)
            track = {
                "track_id": track_id,
                "track_name": resp_json["name"],
                "artist_name": resp_json["artists"][0]["name"],
                "album_art": resp_json["album"]["images"][0],
                "sentiment_score": sentiment_score
            }
            return track
