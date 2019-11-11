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
    def request_tokens(self, code):
        
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

    def refresh_token(self, code):
        url = 'https://accounts.spotify.com/api/token'
        payload = {'grant_type': 'refresh_token', 'refresh_token': code}
        headers = {'Authorization': 'Authorization: Basic '+self.client_b64}
        response = requests.post(url, headers=headers, params=payload)
        # TODO: put this access_token somewhere
        response['access_token']
