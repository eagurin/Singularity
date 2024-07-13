## tests/api/test_training.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_training():
    response = client.post('/api/v1/training/', json={'title': 'test_training', 'content': 'test_content'})
    assert response.status_code == 201
    assert response.json()['title'] == 'test_training'
    assert response.json()['content'] == 'test_content'

def test_get_training():
    # First, create the training to ensure it exists
    client.post('/api/v1/training/', json={'title': 'test_training', 'content': 'test_content'})
    
    response = client.get('/api/v1/training/test_training')
    assert response.status_code == 200
    assert response.json()['title'] == 'test_training'
    assert response.json()['content'] == 'test_content'

def test_delete_training():
    # First, create the training to ensure it exists
    client.post('/api/v1/training/', json={'title': 'test_training', 'content': 'test_content'})
    
    response = client.delete('/api/v1/training/test_training')
    assert response.status_code == 204

    # Verify the training has been deleted
    response = client.get('/api/v1/training/test_training')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Training not found'
