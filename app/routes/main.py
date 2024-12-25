from flask import Blueprint, render_template
from app.services.product_service import get_featured_products

main = Blueprint('main', __name__)

@main.route('/')
def index():
    featured_products = get_featured_products()
    return render_template('pages/index.html', 
                         featured_products=featured_products) 