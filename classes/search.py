from config import Config
from classes.users import search_users
from classes.spotify_helper import SpotifyHelper
import requests


class Search:

    @staticmethod
    def search(query):
        tracks = SpotifyHelper.search_spotify(query)
        users = search_users(query)
        return {
            "tracks": tracks,
            "users": users
        }
