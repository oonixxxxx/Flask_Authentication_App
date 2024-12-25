import os
import sys
import pytest
from app import create_app, db
from app.models import User, Product

# Добавляем путь к корневой директории проекта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def app():
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        # Создаем тестовые данные
        create_test_data()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

def create_test_data():
    """Создание тестовых данных"""
    # Создаем тестового пользователя
    user = User(
        username='testuser',
        email='test@example.com'
    )
    user.set_password('password123')
    db.session.add(user)
    
    # Создаем тестовые продукты
    products = [
        Product(
            name='iPhone 16 Pro',
            price=119990,
            description='Новый iPhone',
            is_featured=True
        ),
        Product(
            name='MacBook Air M2',
            price=129990,
            description='Ноутбук Apple',
            is_featured=True
        )
    ]
    db.session.bulk_save_objects(products)
    db.session.commit() 