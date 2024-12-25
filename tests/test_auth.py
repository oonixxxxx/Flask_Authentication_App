import pytest
from flask_login import current_user

def test_login_page(client):
    """Тест страницы входа"""
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Войти' in response.data

def test_successful_login(client):
    """Тест успешного входа"""
    response = client.post('/login', data={
        'email': 'test@example.com',
        'password': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Успешный вход' in response.data

def test_invalid_login(client):
    """Тест неудачного входа"""
    response = client.post('/login', data={
        'email': 'wrong@example.com',
        'password': 'wrongpass'
    }, follow_redirects=True)
    assert b'Неверный email или пароль' in response.data 