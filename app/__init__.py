from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from flask_jwt_extended import JWTManager
from celery import Celery
from .config import config

# Инициализация расширений Flask
db = SQLAlchemy()         # ORM для работы с базой данных
migrate = Migrate()       # Управление миграциями БД
cache = Cache()          # Система кэширования
jwt = JWTManager()       # Управление JWT токенами
celery = Celery()        # Очередь задач для асинхронных операций

def create_app(config_name='development'):
    """
    Фабричная функция для создания экземпляра Flask приложения
    Args:
        config_name (str): Имя конфигурации ('development', 'production', 'testing')
    Returns:
        Flask: Настроенное Flask приложение
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Инициализация всех расширений с приложением
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    jwt.init_app(app)
    
    # Настройка Celery для асинхронных задач
    celery.conf.update(app.config)
    
    # Регистрация модулей приложения
    from .routes import register_blueprints
    register_blueprints(app)
    
    # Регистрация обработчиков ошибок
    from .errors import register_error_handlers
    register_error_handlers(app)
    
    return app