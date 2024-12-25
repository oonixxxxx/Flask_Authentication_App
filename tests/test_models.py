from app.models import User, Product

def test_user_password_hashing():
    """Тест хеширования пароля"""
    from app.models import User
    
    user = User(email='test@example.com', username='test')
    user.set_password('password123')
    
    assert user.check_password('password123')
    assert not user.check_password('wrong_password')

def test_user_to_dict():
    """Тест сериализации пользователя"""
    from app.models import User
    
    user = User(
        email='test@example.com',
        username='test',
        is_admin=True
    )
    
    data = user.to_dict()
    assert data['email'] == 'test@example.com'
    assert data['username'] == 'test'
    assert data['is_admin'] is True

def test_product_is_in_stock():
    """Тест проверки наличия товара"""
    product = Product(name='Test', price=100, stock=5)
    assert product.is_in_stock is True
    product.stock = 0
    assert product.is_in_stock is False 