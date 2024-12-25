from flask_login import login_user
from app.utils.decorators import admin_required

def test_admin_required(client, app):
    """Тест декоратора admin_required"""
    from app.models import User
    
    with app.test_request_context():
        # Создаем обычного пользователя
        user = User.query.filter_by(email='test@example.com').first()
        login_user(user)
        
        response = client.get('/admin')
        assert response.status_code == 403
        
        # Делаем пользователя админом
        user.is_admin = True
        response = client.get('/admin')
        assert response.status_code == 200 