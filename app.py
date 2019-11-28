from flask import Flask, Blueprint
from api import api_routes
from config import Config
from search import Search
import threading

app = Flask(__name__)
app.register_blueprint(api_routes)
app.config['WTF_CSRF_ENABLED'] = False

# SET AUTH TOKEN AND REFRESH EVERY 3600 seconds
Config.setAuthToken()
threading.Timer(3600, Config.setAuthToken).start()


@app.route("/")
def home():
    return 'Hello worlds'


if __name__ == "__main__":
    app.run(debug=True)
