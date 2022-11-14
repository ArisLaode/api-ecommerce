from flask import Blueprint, jsonify, request, abort
from werkzeug.utils import secure_filename
from extensions import db, save_images
from ..models.product import Products
from ..schema.schema import product_schema

bp_product = Blueprint('bp_product', __name__)


@bp_product.route('/create', methods=["POST"])
def create_product():
    if not request.form:
        abort(400, description="Resource not found")
    images_product = request.files['images']
    if images_product.filename == '':
        return jsonify({"message": "images not found"}), 404
    filename_images = secure_filename(images_product.filename)

    logo_product = request.files['logo']
    if logo_product.filename == '':
        return jsonify({"message": "logo not found"}), 404
    filename_logo = secure_filename(logo_product.filename)
    product = Products(
        name=request.form['name'],
        description=request.form['description'],
        images=filename_images,
        logo_id=filename_logo
    )
    save_images(images_product)
    save_images(logo_product)
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "create success"}), 201


@bp_product.route('/read', methods=["GET"])
def get_all_product():
    query_products = Products.query.all()
    result_products = product_schema.dump(query_products)
    return result_products
