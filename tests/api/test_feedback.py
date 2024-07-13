## tests/api/test_feedback.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_feedback():
    response = client.post('/api/v1/feedback/', json={'user': 'test_user', 'content': 'test_content'})
    assert response.status_code == 201
    assert response.json()['user'] == 'test_user'
    assert response.json()['content'] == 'test_content'

def test_get_feedback():
    # First, create the feedback to ensure it exists
    client.post('/api/v1/feedback/', json={'user': 'test_user', 'content': 'test_content'})
    
    response = client.get('/api/v1/feedback/test_user')
    assert response.status_code == 200
    assert response.json()['user'] == 'test_user'
    assert response.json()['content'] == 'test_content'

def test_delete_feedback():
    # First, create the feedback to ensure it exists
    client.post('/api/v1/feedback/', json={'user': 'test_user', 'content': 'test_content'})
    
    response = client.delete('/api/v1/feedback/test_user')
    assert response.status_code == 204

    # Verify the feedback has been deleted
    response = client.get('/api/v1/feedback/test_user')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Feedback not found'
