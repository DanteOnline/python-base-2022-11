def test_item_list(client):
    response = client.get('/items/')
    assert response.status_code == 200
