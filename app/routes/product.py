from flask import Blueprint, jsonify

product = Blueprint('product', __name__)


@product.route('/product', methods=["GET"])
def index():
    result = {
        'id': 1,
        'name': 'apple',
        'description': 'apple is technology product one of the best!'

    }
    return jsonify(result)
