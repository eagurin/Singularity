## tests/api/test_groups.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_group():
    response = client.post('/api/v1/groups/', json={'name': 'test_group', 'members': ['member1', 'member2']})
    assert response.status_code == 201
    assert response.json()['name'] == 'test_group'
    assert response.json()['members'] == ['member1', 'member2']

def test_get_group():
    # First, create the group to ensure it exists
    client.post('/api/v1/groups/', json={'name': 'test_group', 'members': ['member1', 'member2']})
    
    response = client.get('/api/v1/groups/test_group')
    assert response.status_code == 200
    assert response.json()['name'] == 'test_group'
    assert response.json()['members'] == ['member1', 'member2']

def test_delete_group():
    # First, create the group to ensure it exists
    client.post('/api/v1/groups/', json={'name': 'test_group', 'members': ['member1', 'member2']})
    
    response = client.delete('/api/v1/groups/test_group')
    assert response.status_code == 204

    # Verify the group has been deleted
    response = client.get('/api/v1/groups/test_group')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Group not found'
