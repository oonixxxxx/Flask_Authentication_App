from app import db
from .mixins import TimestampMixin, SoftDeleteMixin
from sqlalchemy.ext.hybrid import hybrid_property

class Product(db.Model, TimestampMixin, SoftDeleteMixin):
    """
    Модель продукта в магазине
    
    Attributes:
        id (int): Уникальный идентификатор продукта
        name (str): Название продукта
        slug (str): URL-friendly идентификатор
        description (str): Описание продукта
        price (Decimal): Цена продукта
        stock (int): Количество на складе
        image_url (str): URL изображения продукта
        is_featured (bool): Флаг для отображения на главной странице
        category_id (int): ID категории продукта
    """
    __tablename__ = 'products'
    
    # Основные поля модели
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, index=True)
    slug = db.Column(db.String(100), unique=True, index=True)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String(200))
    is_featured = db.Column(db.Boolean, default=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    
    # Отношения с другими моделями
    category = db.relationship('Category', back_populates='products')
    
    @hybrid_property
    def is_in_stock(self) -> bool:
        """Проверяет наличие товара на складе"""
        return self.stock > 0
    
    def to_dict(self) -> dict:
        """
        Сериализует объект продукта в словарь
        Returns:
            dict: Словарь с данными продукта
        """
        return {
            'id': self.id,
            'name': self.name,
            'price': float(self.price),
            'is_in_stock': self.is_in_stock,
            'image_url': self.image_url
        } 