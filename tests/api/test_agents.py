## tests/api/test_agents.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_agent():
    response = client.post('/api/v1/agents/', json={'name': 'test_agent', 'model': 'test_model'})
    assert response.status_code == 201
    assert response.json()['name'] == 'test_agent'
    assert response.json()['model'] == 'test_model'

def test_get_agent():
    # First, create the agent to ensure it exists
    client.post('/api/v1/agents/', json={'name': 'test_agent', 'model': 'test_model'})
    
    response = client.get('/api/v1/agents/test_agent')
    assert response.status_code == 200
    assert response.json()['name'] == 'test_agent'
    assert response.json()['model'] == 'test_model'

def test_delete_agent():
    # First, create the agent to ensure it exists
    client.post('/api/v1/agents/', json={'name': 'test_agent', 'model': 'test_model'})
    
    response = client.delete('/api/v1/agents/test_agent')
    assert response.status_code == 204

    # Verify the agent has been deleted
    response = client.get('/api/v1/agents/test_agent')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Agent not found'
