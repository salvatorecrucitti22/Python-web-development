import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

detail = [
    {
        'name': 'API',
        'lastname': 'work'
    },
    {
        'name': 'API2',
        'lastname': 'work2'
    }
]


@app.route('/', methods=['GET'])
def home():
    return '''API Work</h1>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(detail)

app.run()