from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

def register_api_routes(app):
    from . import product_routes
    app.register_blueprint(api) 