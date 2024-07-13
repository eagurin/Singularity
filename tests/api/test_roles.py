## tests/api/test_roles.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_role():
    response = client.post('/api/v1/roles/', json={'name': 'test_role', 'description': 'test_description'})
    assert response.status_code == 201
    assert response.json()['name'] == 'test_role'
    assert response.json()['description'] == 'test_description'

def test_get_role():
    # First, create the role to ensure it exists
    client.post('/api/v1/roles/', json={'name': 'test_role', 'description': 'test_description'})
    
    response = client.get('/api/v1/roles/test_role')
    assert response.status_code == 200
    assert response.json()['name'] == 'test_role'
    assert response.json()['description'] == 'test_description'

def test_delete_role():
    # First, create the role to ensure it exists
    client.post('/api/v1/roles/', json={'name': 'test_role', 'description': 'test_description'})
    
    response = client.delete('/api/v1/roles/test_role')
    assert response.status_code == 204

    # Verify the role has been deleted
    response = client.get('/api/v1/roles/test_role')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Role not found'
