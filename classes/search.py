"""
Executes queries on Spotify to collate search results
"""
import spotify_helper

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
        results = spotify_helper.query(url, params)
        # TODO: find the spotify endpoint for this
        return results