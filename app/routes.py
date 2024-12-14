from flask import render_template
from .models import Product, db

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products) 