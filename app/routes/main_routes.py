from flask import render_template, Blueprint

main = Blueprint('main', __name__)
product_service = None  # Инициализируем позже

@main.route('/')
def index():
    return render_template('pages/index.html')

@main.route('/catalog')
def catalog():
    return render_template('pages/catalog.html')

@main.route('/product/<int:product_id>')
def product(product_id):
    return render_template('pages/product.html') 