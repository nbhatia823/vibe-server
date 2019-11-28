import os
import requests


class Config:
    HOST = 'ec2-174-129-253-140.compute-1.amazonaws.com'
    DATABASE = 'd9ku25a2bulpk2'
    USERNAME = 'bvxxebjsjrhphb'
    PASSWORD = '596f67861a11f2d606078c579ee8aa2f8c8855297aff08e3d0a3f60d1b0f8eed'
    PORT = '5432'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SPOTIFY_CLIENT_ID = '5ae1d35a487842fcbef9cb7f164ec3fb'
    SPOTIFY_CLIENT_SECRET = 'c27f32c0e5f04c2e989acc4c05097ba5'
    SPOTIFY_AUTH_TOKEN = ''

    @staticmethod
    def setAuthToken():
        url = "https://accounts.spotify.com/api/token"
        body_params = {'grant_type': 'client_credentials'}
        authorization = (Config.SPOTIFY_CLIENT_ID,
                         Config.SPOTIFY_CLIENT_SECRET)
        resp = requests.post(url, data=body_params, auth=authorization)
        Config.SPOTIFY_AUTH_TOKEN = resp.json()["access_token"]
