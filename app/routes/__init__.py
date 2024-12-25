from flask import Blueprint
from .main_routes import main
from .auth.views import auth
from .api.product_routes import api
from .admin_routes import admin

def register_blueprints(app):
    """Регистрация всех blueprints"""
    from .main_routes import main
    from .auth.views import auth
    from .api.product_routes import api
    from .admin_routes import admin
    
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(admin) 