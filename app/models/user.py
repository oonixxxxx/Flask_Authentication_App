from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .mixins import TimestampMixin, SoftDeleteMixin

class User(UserMixin, db.Model, TimestampMixin, SoftDeleteMixin):
    """Модель пользователя"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, default=True)
    
    def set_password(self, password):
        """Хеширование пароля"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Проверка пароля"""
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'

@login_manager.user_loader
def load_user(id):
    """Загрузка пользователя для Flask-Login"""
    return User.query.get(int(id)) 