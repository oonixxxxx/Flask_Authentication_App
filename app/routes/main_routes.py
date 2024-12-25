from flask import render_template, Blueprint
from app.services import ProductService

main = Blueprint('main', __name__)
product_service = ProductService()

@main.route('/')
def index():
    featured_products = product_service.get_featured_products()
    return render_template('pages/index.html', featured_products=featured_products)

@main.route('/catalog')
def catalog():
    return render_template('pages/catalog.html', title='Каталог')

@main.route('/product/<int:product_id>')
def product(product_id):
    product = product_service.get_product_by_id(product_id)
    return render_template('pages/product.html', product=product) 