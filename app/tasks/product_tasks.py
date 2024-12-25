from app import celery
from app.services import ProductService
from app.utils.email import send_email

@celery.task
def update_product_stock(product_id: int, quantity: int):
    product_service = ProductService()
    product = product_service.update_stock(product_id, quantity)
    
    if product.stock < product.min_stock_threshold:
        send_email(
            'Low Stock Alert',
            f'Product {product.name} is running low on stock'
        ) 