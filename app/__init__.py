from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_caching import Cache

db = SQLAlchemy()
migrate = Migrate()
cache = Cache()
login_manager = LoginManager()

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Загрузка конфигурации
    from .config import config
    app.config.from_object(config[config_name])
    
    # Инициализация расширений
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    login_manager.init_app(app)
    
    # Регистрация blueprints
    from .routes import register_blueprints
    register_blueprints(app)
    
    return app