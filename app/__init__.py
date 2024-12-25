from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from celery import Celery
from app.config import config

# Инициализация расширений
db = SQLAlchemy()
migrate = Migrate()
cache = Cache()
jwt = JWTManager()
celery = Celery()
login_manager = LoginManager()

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Инициализация расширений
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    jwt.init_app(app)
    login_manager.init_app(app)
    
    # Настройка Celery
    celery.conf.update(app.config)
    
    # Регистрация blueprints
    from .routes import register_blueprints
    register_blueprints(app)
    
    return app