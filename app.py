from flask import Flask, Blueprint
from api import api_routes
from config import Config
from classes.search import Search
import threading
from classes.spotify_helper import SpotifyHelper
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.register_blueprint(api_routes)
app.config['WTF_CSRF_ENABLED'] = False

# SET AUTH TOKEN AND REFRESH EVERY 3600 seconds
Config.setAuthToken()


@app.route("/")
def home():
    return 'Hello worlds'


if __name__ == "__main__":
    app.run(debug=True)
