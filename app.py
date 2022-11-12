from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    result = {
        'id': 1,
        'name': 'apple',
        'description:': 'apple is technology product one of the best in the world!'

    }
    return jsonify(result)


if __name__ == '__main__':
    app.run()
