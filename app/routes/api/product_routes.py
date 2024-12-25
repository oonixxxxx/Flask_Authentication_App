from flask import jsonify
from . import api
from app.services import ProductService

product_service = ProductService()

@api.route('/products')
def get_products():
    products = product_service.get_featured_products()
    return jsonify([p.to_dict() for p in products])

@api.route('/products/<int:product_id>')
def get_product(product_id):
    product = product_service.get_product_by_id(product_id)
    return jsonify(product.to_dict()) 