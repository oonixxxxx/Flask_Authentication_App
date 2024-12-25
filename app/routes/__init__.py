from flask import Blueprint

main = Blueprint('main', __name__)

def register_blueprints(app):
    """Регистрация всех blueprints"""
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(admin) 