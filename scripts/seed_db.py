from app import create_app
from app.models import db, Product

app = create_app()

with app.app_context():
    # Очищаем существующие данные
    db.session.query(Product).delete()
    
    # Добавляем тестовые товары
    products = [
        Product(
            name='Товар 1',
            price=1999.99,
            description='Описание товара 1',
            image_url='/static/images/product1.jpg'
        ),
        Product(
            name='Товар 2',
            price=2999.99,
            description='Описание товара 2',
            image_url='/static/images/product2.jpg'
        ),
        Product(
            name='Товар 3',
            price=3999.99,
            description='Описание товара 3',
            image_url='/static/images/product3.jpg'
        ),
    ]
    
    db.session.add_all(products)
    db.session.commit() 