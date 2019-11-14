"""
Executes queries on Spotify to collate search results
"""
from classes.spotify_helper import SpotifyAPI

class Search:
    """Takes a string query
    Returns a dictionary {users: [list], songs: [list]}
    """
    def getSearchResults(self, query: str):
        pass

    def findUsers(self, query: str):
        results = []
        # TODO: search database to match query with user names
        # append the id's to the results
        # terminate once results hits 5?
        return results

    def findSongs(self, query):
        url = ''
        params = ''
        results = SpotifyAPI.query(url, params)
        # TODO: find the spotify endpoint for this
        return results