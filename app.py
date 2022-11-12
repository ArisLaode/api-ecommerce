from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resource={
    r"/*": {
        "origins": "*"
    }
})


@app.route('/')
def hello_world():
    result = {
        'id': 1,
        'name': 'apple',
        'description': 'apple is technology product one of the best in the world!'

    }
    return jsonify(result)


if __name__ == '__main__':
    app.run()
