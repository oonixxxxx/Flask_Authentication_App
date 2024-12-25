from flask_login import login_user
from app.utils.decorators import admin_required

def test_admin_required(client, app):
    """Тест декоратора admin_required"""
    from app.models import User
    from app import db
    
    with app.test_request_context():
        # Создаем обычного пользователя
        user = User.query.filter_by(email='test@example.com').first()
        login_user(user)
        
        # Проверяем доступ без прав админа
        response = client.get('/admin/')
        assert response.status_code == 403
        
        # Делаем пользователя админом
        user.is_admin = True
        db.session.commit()
        
        # Проверяем доступ с правами админа
        response = client.get('/admin/')
        assert response.status_code == 200 