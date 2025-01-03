import pytest
from flask_login import current_user

def test_login_page(client):
    """Тест страницы входа"""
    response = client.get('/auth/login')
    assert response.status_code == 200
    assert 'Войти' in response.get_data(as_text=True)

def test_successful_login(client):
    """Тест успешного входа"""
    response = client.post('/auth/login', data={
        'email': 'test@example.com',
        'password': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'Успешный вход' in html

def test_invalid_login(client):
    """Тест неудачного входа"""
    response = client.post('/auth/login', data={
        'email': 'wrong@example.com',
        'password': 'wrongpass'
    }, follow_redirects=True)
    html = response.get_data(as_text=True)
    assert 'Неверный email или пароль' in html 