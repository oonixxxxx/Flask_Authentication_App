# -*- coding: utf-8 -*-
import pytest
from app import create_app, db
from app.models import User

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