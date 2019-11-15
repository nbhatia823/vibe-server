from flask import request, json, Response, Blueprint
from classes.users import Users, create_user, get_user, update_user, delete_user
from classes.track import Track, create_track, get_track, update_track, delete_track
from classes.spotify_helper import SpotifyAPI

api_routes = Blueprint('api_routes', __name__)

### USER API ###
@api_routes.route('/api/users', methods=['POST'])
def user_post_handler():
    """
    Creates a new user
    Input: HTTP POST request with JSON body of parameters
    Output: HTTP Response, status 201 if successful, 400 if failed
    """
    if request.method == 'POST':
        print("attempting to post new request")
        user_field_mappings = get_json_body_from_current_request()
        new_user_id = create_user(user_field_mappings)
        if new_user_id != -1:
            print("new user id is ", new_user_id)
            return Response(status=201)
        else:
            return Response(status=400)

@api_routes.route('/api/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_get_or_update_or_delete_handler(user_id): # 'user_id' is string-type
    print("received user request for id ", user_id)
    print("are types equal", (102123121111 == user_id), (user_id == "102123121111" ))
    if request.method == 'GET':
        user_dict = get_user(user_id)
        # if the user with given id exists, send it back as json
        if user_dict:
            user_json = json.dumps(user_dict)
            return Response(user_json,
                        mimetype='application/json',
                        status=200)
        # else if not found, return 404 code saying not found
        else:
            return Response(status=404)

    elif request.method == 'PUT':
        user_field_mappings = get_json_body_from_current_request()
        rows_updated = update_user(user_id, user_field_mappings)
        print(rows_updated)
        if rows_updated == 1:
            return Response(status=204)
        else:
            return Response(status=400)

    elif request.method == 'DELETE':
        rows_deleted = delete_user(user_id)
        if rows_deleted == 1:
            return Response(status=204)
        else:
            return Response(status=400)


### TRACK API ###

@api_routes.route('/api/track', methods=['POST'])
def post_track_handler():
    if request.method == 'POST':
        print("attempting to post new request")
        track_field_mappings = get_json_body_from_current_request()
        new_track_id = create_track(track_field_mappings)
        if new_track_id != -1:
            return Response(status=201)
        else:
            return Response(status=400)

@api_routes.route('/api/track/<track_id>', methods=['PUT', 'GET', 'DELETE'])
def track_get_or_update_or_delete_handler(track_id): # 'id' is string-type ?
    print("received track request for id ", track_id)

    if request.method == 'GET':
        track_dict = get_track(track_id)
        # if the track with given id exists, send it back as json;
        if track_dict:
            track_json = json.dumps(track_dict)
            return Response(track_json,
                        mimetype='application/json',
                        status=200)
        # else if not found, return 404 code saying not found
        else:
            return Response(status=404)

    elif request.method == 'PUT':
        track_field_mappings = get_json_body_from_current_request()
        rows_updated = update_track(track_id, track_field_mappings)
        if rows_updated == 1:
            return Response(status=204)
        else:
            return Response(status=400)

    elif request.method == 'DELETE':
        rows_deleted = delete_track(track_id)
        if rows_deleted == 1:
            return Response(status=204)
        else:
            return Response(status=400)


# reads field_mappings from body of request and returns as a dictionary of field_name: field_value;
# must be a json-type header in request
def get_json_body_from_current_request():
    field_mappings = request.json
    return field_mappings


### Spotify Redirect URI ###
@api_routes.route('/api/spotify_callback', methods=['GET'])
#TODO: how to make these function definitions?
def handler():
    # we get a code to exchange for access token
    #TODO: parse the response query string for error and code?
    code = 1
    helper = SpotifyAPI()
    helper.request_user_tokens(code)
