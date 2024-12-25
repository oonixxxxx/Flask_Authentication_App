from app import db, cache
from app.models import Product
from app.utils.exceptions import ProductNotFoundError
from typing import List, Optional

class ProductService:
    """
    Сервисный слой для работы с продуктами
    
    Предоставляет методы для работы с продуктами,
    включая кэширование и бизнес-логику
    """
    
    @cache.memoize(timeout=300)
    def get_featured_products(self) -> List[Product]:
        """
        Получает список рекомендуемых продуктов
        
        Returns:
            List[Product]: Список активных рекомендуемых продуктов
        """
        return Product.query.filter_by(
            is_featured=True, 
            deleted_at=None
        ).order_by(Product.created_at.desc()).all()
    
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        """
        Получает продукт по ID
        
        Args:
            product_id (int): ID продукта
            
        Returns:
            Product: Объект продукта
            
        Raises:
            ProductNotFoundError: Если продукт не найден
        """
        product = Product.query.get(product_id)
        if not product or product.deleted_at:
            raise ProductNotFoundError(f"Product with id {product_id} not found")
        return product
    
    @cache.memoize(timeout=3600)
    def get_products_by_category(self, category_id: int) -> List[Product]:
        """
        Получает список продуктов в категории
        
        Args:
            category_id (int): ID категории
            
        Returns:
            List[Product]: Список продуктов в категории
        """
        return Product.query.filter_by(
            category_id=category_id,
            deleted_at=None
        ).all() 