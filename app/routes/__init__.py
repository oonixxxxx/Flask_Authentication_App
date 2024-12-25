from flask import Blueprint

main = Blueprint('main', __name__)

def register_blueprints(app):
    from .main_routes import main
    from .auth import auth
    from .api import api
    
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(api) 