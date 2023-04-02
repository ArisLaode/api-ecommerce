from flask import Blueprint, jsonify, request, abort
from werkzeug.utils import secure_filename
from extensions import db, save_images
from ..models.variant import Variants
from ..schema.schema import variants_schema, variants_schema_by_id

bp_variant = Blueprint('bp_variant', __name__)


@bp_variant.route('/create', methods=["POST"])
def create_variant():
    product_id_ = request.form['product_id']
    name_variant = request.form['name']
    size_variant = request.form['size']
    color_variant = request.form['color']
    images_variant = request.files['images']
    if not product_id_:
        return jsonify({"message": "product id not found"}), 404
    if not name_variant:
        return jsonify({"message": "name variant not found"}), 404
    if not size_variant:
        return jsonify({"message": "size variant not found"}), 404
    if not color_variant:
        return jsonify({"message": "color variant not found"}), 404
    if not images_variant:
        return jsonify({"message": "images variant not found"}), 404

    filename_images = secure_filename(images_variant.filename)
    variant = Variants(
        product_id=product_id_,
        name=name_variant,
        size=size_variant,
        color=color_variant,
        images=filename_images
    )
    save_images(images_variant)
    db.session.add(variant)
    db.session.commit()
    return jsonify({"message": "create variant success"}), 201


@bp_variant.route('/read', methods=["GET"])
def get_all_variant():
    query_variants = Variants.query.all()
    result_variants = variants_schema.dump(query_variants)
    return result_variants, 200


@bp_variant.route('read/<int:id_>', methods=["GET"])
def get_variant_id(id_):
    query_variant_by_id = Variants.query.filter_by(id=id_).first()
    if not query_variant_by_id:
        return jsonify({"message": "variant not exist!"}), 404
    result_variant_by_id = variants_schema_by_id.dump(query_variant_by_id)
    return result_variant_by_id, 200


@bp_variant.route('update/<int:id_>', methods=["PUT"])
def update_variant(id_):
    product_id_ = request.form['product_id']
    name_variant = request.form['name']
    size_variant = request.form['size']
    color_variant = request.form['color']
    images_variant = request.files['images']
    filename_images = secure_filename(images_variant.filename)
    query_variant = Variants.query.filter_by(id=id_).first()
    if not query_variant:
        return jsonify({"message": "variant not exist!"}), 404
    query_variant.product_id = product_id_,
    query_variant.name = name_variant,
    query_variant.size = size_variant,
    query_variant.color = color_variant,
    query_variant.images = filename_images
    save_images(images_variant)
    db.session.commit()
    return jsonify({"message": "update variant success"}), 200
