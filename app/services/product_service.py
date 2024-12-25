from app import db, cache
from app.models import Product
from app.utils.exceptions import ProductNotFoundError
from typing import List, Optional

class ProductService:
    """Сервисный слой для работы с продуктами"""
    
    @cache.memoize(timeout=300)
    def get_featured_products(self) -> List[Product]:
        """Получает список рекомендуемых продуктов"""
        return Product.query.filter_by(
            is_featured=True, 
            deleted_at=None
        ).order_by(Product.created_at.desc()).all()
    
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        """Получает продукт по ID"""
        product = Product.query.filter_by(id=product_id, deleted_at=None).first()
        if not product:
            raise ProductNotFoundError(f"Product with id {product_id} not found")
        return product
    
    @cache.memoize(timeout=3600)
    def get_products_by_category(self, category_id: int) -> List[Product]:
        """Получает список продуктов в категории"""
        return Product.query.filter_by(
            category_id=category_id,
            deleted_at=None
        ).all() 