## tests/api/test_recommendations.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_recommendation():
    response = client.post('/api/v1/recommendations/', json={'title': 'test_recommendation', 'content': 'test_content'})
    assert response.status_code == 201
    assert response.json()['title'] == 'test_recommendation'
    assert response.json()['content'] == 'test_content'

def test_get_recommendation():
    # First, create the recommendation to ensure it exists
    client.post('/api/v1/recommendations/', json={'title': 'test_recommendation', 'content': 'test_content'})
    
    response = client.get('/api/v1/recommendations/test_recommendation')
    assert response.status_code == 200
    assert response.json()['title'] == 'test_recommendation'
    assert response.json()['content'] == 'test_content'

def test_delete_recommendation():
    # First, create the recommendation to ensure it exists
    client.post('/api/v1/recommendations/', json={'title': 'test_recommendation', 'content': 'test_content'})
    
    response = client.delete('/api/v1/recommendations/test_recommendation')
    assert response.status_code == 204

    # Verify the recommendation has been deleted
    response = client.get('/api/v1/recommendations/test_recommendation')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Recommendation not found'
