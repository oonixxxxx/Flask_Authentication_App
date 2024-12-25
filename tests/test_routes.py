def test_index_page(client):
    """Тест главной страницы"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'ONIX HUB' in response.data
    assert b'iPhone 16 Pro' in response.data
    assert b'MacBook Air M2' in response.data

def test_catalog_page(client):
    """Тест страницы каталога"""
    response = client.get('/catalog')
    assert response.status_code == 200
    assert b'Каталог' in response.data

def test_product_page(client):
    """Тест страницы продукта"""
    response = client.get('/product/1')
    assert response.status_code == 200
    assert b'iPhone 16 Pro' in response.data 