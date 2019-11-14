### Project Description
This is the backend for the Vibe server. 

### Directory Structure
This is a Flask project. The root directory contains the core Flask .py files, such as app.py.
The class api.py contains our routes. For every valid HTTP request, we have a handler function that delegates a majority of the work to our internal classes.
In `classes/` we have the internal class structure for our app. This implementation follows our UML diagram.
In `test_app/` we have the code for our unit tests.


### Setup
You can use a virtualenv if you want, but there are pip requirements outlined in requirements.txt to be fulfilled.

Run `pip install -r requirements.txt` to get the packages.

The Spotify API configuration is in spotify_helper.py.
