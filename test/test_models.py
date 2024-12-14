import unittest
from main import db, User

class TestModels(unittest.TestCase):
    def setUp(self):
        """Настройка тестовой базы данных"""
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        """Очистка после тестов"""
        db.session.remove()
        db.drop_all()

    def test_user_creation(self):
        """Тест создания пользователя"""
        user = User(username='testuser', email='test@test.com')
        user.set_password('testpass')
        db.session.add(user)
        db.session.commit()

        found_user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.email, 'test@test.com')
        self.assertTrue(found_user.check_password('testpass')) 