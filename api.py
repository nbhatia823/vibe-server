from flask import request, json, Response, Blueprint
from classes.user import User, create_user, get_user, update_user, delete_user


api_routes = Blueprint('api_routes', __name__)

### USER API ###
@api_routes.route('/api/user/<user_id>', methods=['GET','POST','PUT'])
def handle_user_request(user_id):
    if request.method == 'GET':
        return User.get_user(user_id)

@api_routes.route('/api/user', methods=['POST'])
def post_user():
    if request.method == 'POST':
        print("attempting to post new request")
        user_field_mappings = get_user_info_from_current_request()
        new_user_id = create_user(user_field_mappings)
        if new_user_id != -1:
            return Response(status=201)
        else:
            return Response(status=400)

@api_routes.route('/api/user/<user_id>', methods=['PUT', 'GET', 'DELETE'])
def get_or_update_or_delete_user(user_id): # 'id' is string-type ?
    
    if request.method == 'PUT':
        user_field_mappings = get_user_info_from_current_request()
        rows_updated = update_user(id, user_field_mappings)
        if rows_updated == 1:
            return Response(status=204)
        else:
            return Response(status=400)
    
    elif request.method == 'GET':
        user_dict = get_user(id)
        # if the user with given id exists, send it back as json;
        if user_dict:
            user_json = json.dumps(user_dict)
            return Response(user_json,  
                        mimetype='application/json', 
                        status=200)
        # else if not found, return 404 code saying not found
        else:
            return Response(status=404)
    
    elif request.method == 'DELETE':
        rows_deleted = delete_user(id)
        if rows_deleted == 1:
            return Response(status=204)
        else:
            return Response(status=400)
            
# reads field_mappings from body of request and returns as a dictionary of field_name: field_value; 
# must be a json-type header in request
def get_user_info_from_current_request():
    field_mappings = request.json
    return field_mappings

