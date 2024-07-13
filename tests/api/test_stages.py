## tests/api/test_stages.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_stage():
    response = client.post('/api/v1/stages/', json={'name': 'test_stage', 'description': 'test_description'})
    assert response.status_code == 201
    assert response.json()['name'] == 'test_stage'
    assert response.json()['description'] == 'test_description'

def test_get_stage():
    # First, create the stage to ensure it exists
    client.post('/api/v1/stages/', json={'name': 'test_stage', 'description': 'test_description'})
    
    response = client.get('/api/v1/stages/test_stage')
    assert response.status_code == 200
    assert response.json()['name'] == 'test_stage'
    assert response.json()['description'] == 'test_description'

def test_delete_stage():
    # First, create the stage to ensure it exists
    client.post('/api/v1/stages/', json={'name': 'test_stage', 'description': 'test_description'})
    
    response = client.delete('/api/v1/stages/test_stage')
    assert response.status_code == 204

    # Verify the stage has been deleted
    response = client.get('/api/v1/stages/test_stage')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Stage not found'
