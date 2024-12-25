from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.services import ProductService
from app.schemas import ProductSchema
from app.utils.decorators import handle_exceptions

class ProductResource(Resource):
    def __init__(self):
        self.product_service = ProductService()
        self.product_schema = ProductSchema()
    
    @handle_exceptions
    def get(self, product_id):
        product = self.product_service.get_product_by_id(product_id)
        return self.product_schema.dump(product)
    
    @jwt_required()
    @handle_exceptions
    def put(self, product_id):
        product = self.product_service.update_product(product_id, request.json)
        return self.product_schema.dump(product) 