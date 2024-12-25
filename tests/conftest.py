# -*- coding: utf-8 -*-
import pytest
from app import create_app, db
from app.models import User, Product

@pytest.fixture
def app():
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        
        # Создаем тестового пользователя
        user = User(
            email='test@example.com',
            username='test_user'
        )
        user.set_password('password123')
        db.session.add(user)
        
        # Создаем тестовые продукты
        products = [
            Product(
                name='iPhone 16 Pro',
                price=119990,
                description='Новый iPhone',
                is_featured=True,
                stock=10
            ),
            Product(
                name='MacBook Air M2',
                price=129990,
                description='Ноутбук Apple',
                is_featured=True,
                stock=5
            )
        ]
        db.session.bulk_save_objects(products)
        db.session.commit()
        
        yield app
        
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner() 