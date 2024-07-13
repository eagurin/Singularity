## tests/api/test_news.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_news():
    response = client.post('/api/v1/news/', json={'title': 'test_news', 'content': 'test_content'})
    assert response.status_code == 201
    assert response.json()['title'] == 'test_news'
    assert response.json()['content'] == 'test_content'

def test_get_news():
    # First, create the news to ensure it exists
    client.post('/api/v1/news/', json={'title': 'test_news', 'content': 'test_content'})
    
    response = client.get('/api/v1/news/test_news')
    assert response.status_code == 200
    assert response.json()['title'] == 'test_news'
    assert response.json()['content'] == 'test_content'

def test_delete_news():
    # First, create the news to ensure it exists
    client.post('/api/v1/news/', json={'title': 'test_news', 'content': 'test_content'})
    
    response = client.delete('/api/v1/news/test_news')
    assert response.status_code == 204

    # Verify the news has been deleted
    response = client.get('/api/v1/news/test_news')
    assert response.status_code == 404
    assert response.json()['detail'] == 'News not found'
