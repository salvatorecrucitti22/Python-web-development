import flask
from flask import Flask, render_template, Response, request, redirect, url_for

app = flask.Flask(__name__)
app.config["DEBUG"] = True

detail = [
    {
        'id': 0,
        'name': 'API',
        'lastname': 'work'
    },
    {
        'id': 1,
        'name': 'API2',
        'lastname': 'work2'
    }
]


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html');


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/detail/all', methods=['GET'])
def api_all():
    return jsonify(detail)


@app.route('/api/v1/resources/detail', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for detl in detail:
        if detl['id'] == id:
            results.append(detl)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


app.run()