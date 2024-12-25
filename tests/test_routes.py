def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'ONIX HUB' in response.data 