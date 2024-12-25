from flask import render_template
from . import main
from app.services.product_service import ProductService

product_service = ProductService()

@main.route('/')
def index():
    featured_products = product_service.get_featured_products()
    return render_template('pages/index.html', 
                         featured_products=featured_products) 