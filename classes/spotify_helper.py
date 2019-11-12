"""Helper class for all Spotify API queries

references:
https://developer.spotify.com/documentation/general/guides/authorization-guide/#authorization-code-flow
"""
import requests, os, base64

class SpotifyAPI:
    client_id = 'CLIENT_ID'
    client_secret = os.environ.get('SPOTIFY_SECRET')
    redirect_uri = ''
    client_b64 = base64.encodestring(client_id+":"+client_secret)

    """
    Step 1: Request authorization from user to access data
    """
    def register_user(self):
        url = 'https://accounts.spotify.com/authorize'
        # required parameters
        payload = {}
        payload['response_type'] = 'code'
        payload['scopes'] = 'user-read-recently-played'
        payload['client_id'] = self.client_id
        # TODO: could also add a cookie with payload['state'] for security
        requests.get(url, params=payload)
    
    """
    Step 2: Got callback from step 1
    Either access denied (error) or
    we get a code that we need to convert to tokens
    """
    def request_user_tokens(self, code):
        
        url = 'https://accounts.spotify.com/api/token'
        headers = {'content-type': 'application/x-www-form-urlencoded',
        'Authorization': 'Authorization: Basic '+self.client_b64}
        payload = {'grant_type': "authorization_code",
         'redirect_uri': self.redirect_uri,
         'code': code}
        response = requests.post(url, headers=headers, params=payload)
        # TODO: put these in our user table?
        response['access_token']
        response['refresh_token']
        response['expires_in']

    def refresh_user_token(self, code):
        url = 'https://accounts.spotify.com/api/token'
        payload = {'grant_type': 'refresh_token', 'refresh_token': code}
        headers = {'Authorization': 'Authorization: Basic '+self.client_b64}
        response = requests.post(url, headers=headers, params=payload)
        # TODO: put this access_token somewhere
        response['access_token']

    """
    https://developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow
    server to server authentication
    can access info that isn't user specific
    """
    def request_server_token(self):
        url = 'https://accounts.spotify.com/api/token'
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        headers['Authorization'] = 'Authorization: Basic '+self.client_b64
        params = {'grant_type': 'client_credentials'}

        response = requests.post(url, headers=headers, params=params)
        self.server_token = response['access_token']
        self.server_token_expires = response['expires_in']

    def get_track_by_id(self, track_id):
        url = 'https://api.spotify.com/v1/tracks/' + str(track_id)

        # TODO: check if server token expired
        if self.server_token is None:
            self.request_server_token()
        headers = {'Authorization': self.server_token}

        requests.get(url, headers=headers)
        # TODO: put all this info into a track object in the DB