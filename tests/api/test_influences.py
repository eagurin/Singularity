## tests/api/test_influences.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_influence():
    response = client.post('/api/v1/influences/', json={'name': 'test_influence', 'effect': 'test_effect'})
    assert response.status_code == 201
    assert response.json()['name'] == 'test_influence'
    assert response.json()['effect'] == 'test_effect'

def test_get_influence():
    # First, create the influence to ensure it exists
    client.post('/api/v1/influences/', json={'name': 'test_influence', 'effect': 'test_effect'})
    
    response = client.get('/api/v1/influences/test_influence')
    assert response.status_code == 200
    assert response.json()['name'] == 'test_influence'
    assert response.json()['effect'] == 'test_effect'

def test_delete_influence():
    # First, create the influence to ensure it exists
    client.post('/api/v1/influences/', json={'name': 'test_influence', 'effect': 'test_effect'})
    
    response = client.delete('/api/v1/influences/test_influence')
    assert response.status_code == 204

    # Verify the influence has been deleted
    response = client.get('/api/v1/influences/test_influence')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Influence not found'
