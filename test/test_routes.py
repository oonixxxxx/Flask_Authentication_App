import unittest
from main import app
import json

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        """Тест главной страницы"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ONIX HUB', response.data)

    def test_login_page(self):
        """Тест страницы входа"""
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_signup_page(self):
        """Тест страницы регистрации"""
        response = self.app.get('/signup')
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        """Тест неверного входа"""
        response = self.app.post('/login', data={
            'username': 'nonexistent',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 401)

    def test_logout(self):
        """Тест выхода из с��стемы"""
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 302)  # Редирект после выхода 