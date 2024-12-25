from flask import Blueprint

main = Blueprint('main', __name__)

def register_blueprints(app):
    from . import main_routes
    app.register_blueprint(main) 