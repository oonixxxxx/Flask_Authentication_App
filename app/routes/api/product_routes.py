from flask import jsonify
from . import api
from app.services import ProductService

product_service = ProductService()

@api.route('/products')
def get_products():
    """Получение списка продуктов"""
    products = product_service.get_featured_products()
    return jsonify([p.to_dict() for p in products])

@api.route('/products/<int:product_id>')
def get_product(product_id):
    """Получение одного продукта"""
    try:
        product = product_service.get_product_by_id(product_id)
        return jsonify(product.to_dict())
    except Exception:
        return jsonify({'error': 'Product not found'}), 404 