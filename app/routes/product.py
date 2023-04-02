from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
from extensions import db, save_images
from ..models.product import Products
from ..schema.schema import product_schema, product_schema_by_id

bp_product = Blueprint('bp_product', __name__)


@bp_product.route('/create', methods=["POST"])
def create_product():
    name_product = request.form['name']
    desc_product = request.form['description']
    images_product = request.files['images']
    logo_product = request.files['logo']

    if not name_product:
        return jsonify({"message": "name not found"}), 404
    elif not images_product:
        return jsonify({"message": "images not found"}), 404
    elif not logo_product:
        return jsonify({"message": "logo not found"}), 404

    filename_images = secure_filename(images_product.filename)
    filename_logo = secure_filename(logo_product.filename)
    product = Products(
        name=name_product,
        description=desc_product,
        images=filename_images,
        logo_id=filename_logo
    )
    save_images(images_product)
    save_images(logo_product)
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "create product success"}), 201


@bp_product.route('/read', methods=["GET"])
def get_all_product():
    query_products = Products.query.all()
    result_products = product_schema.dump(query_products)
    return result_products, 200


@bp_product.route('/read/<int:id_>', methods=["GET"])
def get_product_id(id_):
    query_product_by_id = Products.query.filter_by(id=id_).first()
    if not query_product_by_id:
        return jsonify({"message": "product not exist!"}), 404
    result_product_by_id = product_schema_by_id.dump(query_product_by_id)
    return result_product_by_id, 200


@bp_product.route('/update/<int:id_>', methods=["PUT"])
def update_product(id_):
    name_product = request.form['name']
    desc_product = request.form['description']
    images_product = request.files['images']
    logo_product = request.files['logo']
    query_product = Products.query.filter_by(id=id_).first()
    if not query_product:
        return jsonify({"message": "product not exist!"}), 404
    elif not name_product:
        return jsonify({"message": "name not found"}), 404
    elif not images_product:
        return jsonify({"message": "images not found"}), 404
    elif not logo_product:
        return jsonify({"message": "logo not found"}), 404
    filename_images = secure_filename(images_product.filename)
    filename_logo = secure_filename(logo_product.filename)
    query_product.name = name_product
    query_product.description = desc_product
    query_product.images = filename_images
    query_product.logo = filename_logo
    save_images(images_product)
    save_images(logo_product)
    db.session.commit()
    return jsonify({"message": "update product success"}), 200
