## tests/api/test_tasks.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post('/api/v1/tasks/', json={'name': 'test_task', 'action': 'test_action'})
    assert response.status_code == 201
    assert response.json()['name'] == 'test_task'
    assert response.json()['action'] == 'test_action'

def test_get_task():
    # First, create the task to ensure it exists
    client.post('/api/v1/tasks/', json={'name': 'test_task', 'action': 'test_action'})
    
    response = client.get('/api/v1/tasks/test_task')
    assert response.status_code == 200
    assert response.json()['name'] == 'test_task'
    assert response.json()['action'] == 'test_action'

def test_delete_task():
    # First, create the task to ensure it exists
    client.post('/api/v1/tasks/', json={'name': 'test_task', 'action': 'test_action'})
    
    response = client.delete('/api/v1/tasks/test_task')
    assert response.status_code == 204

    # Verify the task has been deleted
    response = client.get('/api/v1/tasks/test_task')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Task not found'
