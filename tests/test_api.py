import json

def test_get_products(client):
    """Тест API получения продуктов"""
    response = client.get('/api/products')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2
    assert data[0]['name'] == 'iPhone 16 Pro'

def test_get_product(client):
    """Тест API получения одного продукта"""
    response = client.get('/api/products/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'iPhone 16 Pro'

def test_product_not_found(client):
    """Тест получения несуществующего продукта"""
    response = client.get('/api/products/999')
    assert response.status_code == 404 