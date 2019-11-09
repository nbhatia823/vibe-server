from flask import request, json, Response, Blueprint
from classes.user import User

api_routes = Blueprint('pra_api', __name__)

### USER API ###
@api_routes.route('/api/user/<user_id>', methods=['GET','POST','PUT'])
def handle_user_request(user_id):
    if request.method == 'GET':
        return User.get_user(user_id)