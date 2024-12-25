from app.models import User, Product

def test_user_password_hashing():
    """Тест хеширования пароля"""
    user = User(username='test', email='test@test.com')
    user.set_password('cat')
    assert not user.check_password('dog')
    assert user.check_password('cat')

def test_product_is_in_stock():
    """Тест проверки наличия товара"""
    product = Product(name='Test', price=100, stock=5)
    assert product.is_in_stock is True
    product.stock = 0
    assert product.is_in_stock is False 