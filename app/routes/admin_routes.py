from flask import Blueprint, render_template
from app.utils.decorators import admin_required

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
@admin_required
def index():
    """Главная страница админки"""
    return render_template('admin/index.html')

@admin.route('/products')
@admin_required
def products():
    """Управление товарами"""
    return render_template('admin/products.html')

@admin.route('/users')
@admin_required
def users():
    """Управление пользователями"""
    return render_template('admin/users.html') 