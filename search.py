from config import Config
from classes.users import search_users
import requests


class Search:

    @staticmethod
    def searchSpotify(query):
        query.replace(" ", "%20")
        url = f'{Config.SPOTIFY_API_URL}/v1/search?q={query}&type=track&limit=4'
        resp = requests.get(url, headers=Config.SPOTIFY_REQ_HEADERS)
        return resp.json()["tracks"]["items"]

    @staticmethod
    def search(query):
        tracks = Search.searchSpotify(query)
        users = search_users(query)
        return {
            "tracks": tracks,
            "users": users
        }
