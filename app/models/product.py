from app import db
from .mixins import TimestampMixin, SoftDeleteMixin
from sqlalchemy.ext.hybrid import hybrid_property

class Product(db.Model, TimestampMixin, SoftDeleteMixin):
    """Модель продукта"""
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    stock = db.Column(db.Integer, default=0)
    is_featured = db.Column(db.Boolean, default=False)
    
    @hybrid_property
    def is_in_stock(self):
        """Проверяет наличие товара на складе"""
        return self.stock > 0
    
    def __repr__(self):
        return f'<Product {self.name}>' 