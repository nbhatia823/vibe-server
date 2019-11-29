from flask import request, json, Response, Blueprint
from classes.users import Users, get_user, update_user, delete_user, create_user
from classes.track import Track, create_track, get_track, update_track, delete_track
from classes.user_posts import UserPosts, get_all_user_posts, get_current_user_posts, create_user_post, delete_current_user_posts
from classes.friends import Friends, add_friend, delete_friend, get_friends
from classes.search import Search
from classes.spotify_helper import SpotifyHelper
import sys
import time

api_routes = Blueprint('api_routes', __name__)

### SEARCH API ###
@api_routes.route('/api/search', methods=['GET'])
def search_handler():
    if request.method == 'GET':
        query = request.args.get('q')
        if query == None:
            return Response(status=400)
        else:
            data = Search.search(query)
            return Response(json.dumps(data),
                            mimetype='application/json',
                            status=200)


### USER API ###
@api_routes.route('/api/users', methods=['PUT'])
def user_put_handler():
    """
    Creates a new user OR updates user if they already exist
    Input: HTTP POST request with JSON body of parameters
    Output: HTTP Response, status 201 if successful, 400 if failed
    """
    if request.method == 'PUT':
        user_field_mappings = get_json_body_from_current_request()
        user_id = user_field_mappings["user_id"]
        if get_user(user_id) == None:
            # Create user
            rows_updated = create_user(user_field_mappings)
        else:
            # Update user
            rows_updated = update_user(user_id, user_field_mappings)
        if rows_updated != -1:
            return Response(status=204)
        else:
            return Response(status=400)


@api_routes.route('/api/users/<user_id>', methods=['GET', 'DELETE'])
def user_get_or_delete_handler(user_id):  # 'user_id' is string-type
    """
    Gets, updates, or deletes an existing user
    Input: HTTP GET. Output: JSON, status 200, or status 404
    Input: HTTP POST. Output: 204 or 400.
    Input: HTTP DELETE. Output: 204, or 400.
    """

    if request.method == 'GET':
        user_dict = get_user(user_id)
        # if the user with given id exists, send it back as json
        if user_dict:
            return Response(json.dumps(user_dict),
                            mimetype='application/json',
                            status=200)
        # else if not found, return 404 code saying not found
        else:
            return Response(status=404)

    elif request.method == 'DELETE':
        rows_deleted = delete_user(user_id)
        if rows_deleted == 1:
            return Response(status=204)
        else:
            return Response(status=400)


### TRACK API ###
@api_routes.route('/api/track', methods=['POST'])
def post_track_handler():
    """
    Creates a new track
    Input: POST
    Output:  201 if created, 400 otherwise
    """
    if request.method == 'POST':
        track_field_mappings = get_json_body_from_current_request()
        new_track_id = create_track(track_field_mappings)
        if new_track_id != -1:
            return Response(status=201)
        else:
            return Response(status=400)


@api_routes.route('/api/track/<track_id>', methods=['PUT', 'GET', 'DELETE'])
def track_get_or_update_or_delete_handler(track_id):  # 'id' is string-type ?
    """
    Get, update, or delete
    Input: PUT. Output: status 204 or 400.
    Input: GET. Output: JSON + status 200. or status 404
    Input: DELETE. Output: Status 204 or 400.
    """

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


### USER FEED API ###
@api_routes.route('/api/users/<user_id>/post/history', methods=['GET'])
def get_track_of_day_history_handler(user_id):
    """
    Get the history of tracks of the day posted by this user
    """
    if request.method == 'GET':
        user_posts_dicts = get_all_user_posts(user_id)
        if user_posts_dicts != None:
            return Response(json.dumps(user_posts_dicts),
                            mimetype='application/json',
                            status=200)
        else:
            return Response(status=400)


@api_routes.route('/api/users/<user_id>/post/<track_id>', methods=['POST'])
def post_track_of_day_handler(user_id, track_id):
    """Posts the user's track of the day.
    """
    if request.method == 'POST':
        if get_user(user_id):
            new_user_post = {
                "user_id": user_id,
                "track_id": track_id,
                "date_posted": int(round(time.time()*1000))
            }

            if not get_track(track_id):
                # Get track info and add to DB
                track = SpotifyHelper.get_track_by_id(track_id)
                if track:
                    create_track(track)
                else:
                    # Not a valid track id, Bad Request
                    return Response(status=400)

            # Create new user post
            rows_updated = create_user_post(new_user_post)
            if rows_updated == -1:
                return Response(status=400)
            else:
                return Response(status=200)
        else:
            return Response(status=404)


@api_routes.route('/api/users/<user_id>/post', methods=['DELETE'])
def delete_track_of_day_handler(user_id):
    """Remove the user's track of the day.
    Input: HTTP delete
    Output: Response 204 if deleted, or 400 if invalid.
    """
    if request.method == 'DELETE':
        if delete_current_user_posts(user_id) == -1:
            return Response(status=400)
        return Response(status=204)


@api_routes.route('/api/users/<user_id>/feed', methods=['GET'])
def get_user_feed_handler(user_id):
    """Get the songs for a user's feed.
    Input: HTTP GET with user_id
    Output: Return the JSON dictionary of songs for the feed
    """
    if request.method == 'GET':
        pass


@api_routes.route('/api/users/<user_id>/history', methods=['GET'])
def get_recently_played(user_id):
    """
    Get the recently played songs.
    Input: HTTP GET, JSON = TODO: number? songs?
    Output: JSON dictionary
    """
    if request.method == 'GET':
        pass

### FRIENDS API ###
@api_routes.route('/api/users/<user_id>/friends', methods=['GET'])
def get_friend_list_handler(user_id):
    """
    Get the list of friend ids.
    """
    if request.method == 'GET':
        friends_dicts = get_friends(user_id)
        if friends_dicts != None:
            return Response(json.dumps(friends_dicts),
                            mimetype='application/json',
                            status=200)
        else:
            return Response(status=400)


@api_routes.route('/api/users/<user_id>/friends/<friend_id>', methods=['POST', 'DELETE'])
def add_or_delete_friend_handler(user_id, friend_id):
    if request.method == 'POST':
        if add_friend(user_id, friend_id):
            return Response(status=201)
        else:
            return Response(status=400)
    elif request.method == 'DELETE':
        if delete_friend(user_id, friend_id):
            return Response(status=204)
        else:
            return Response(status=400)


# reads field_mappings from body of request and returns as a dictionary of field_name: field_value;
# must be a json-type header in request
def get_json_body_from_current_request():
    field_mappings = request.json
    return field_mappings
