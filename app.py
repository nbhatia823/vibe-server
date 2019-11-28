from flask import Flask, Blueprint
from api import api_routes

app = Flask(__name__)
app.register_blueprint(api_routes)
app.config['WTF_CSRF_ENABLED'] = False


@app.route("/")
def home():
    return 'Hello worlds'


if __name__ == "__main__":
    app.run(debug=True)
