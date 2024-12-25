def test_index_page(client):
    """Тест главной страницы"""
    response = client.get('/')
    assert response.status_code == 200
    assert 'ONIX HUB' in response.get_data(as_text=True)
    assert 'iPhone 16 Pro' in response.get_data(as_text=True)
    assert 'MacBook Air M2' in response.get_data(as_text=True)

def test_catalog_page(client):
    """Тест страницы каталога"""
    response = client.get('/catalog')
    assert response.status_code == 200
    assert 'Каталог' in response.get_data(as_text=True)

def test_product_page(client):
    """Тест страницы продукта"""
    response = client.get('/product/1')
    assert response.status_code == 200
    assert 'iPhone 16 Pro' in response.get_data(as_text=True) 