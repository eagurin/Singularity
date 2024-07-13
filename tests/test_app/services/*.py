"""
This module contains unit tests for the AgentService class.
Ensure the environment is correctly set up with all necessary dependencies installed, including FastAPI.
"""

import unittest
from unittest.mock import MagicMock, patch
from app.services.agent_service import AgentService
from app.models.schemas.agent import AgentCreate, Agent as SchemaAgent

class TestAgentService(unittest.TestCase):
    ## SETUP AND TEARDOWN
    def setUp(self):
        """
        Set up test environment before each test.
        """
        self.mock_db = MagicMock()
        self.agent_service = AgentService(db=self.mock_db)
        self.default_agent_id = 1
        self.default_agent_name = "Test Agent"
        self.default_role_id = 101
        self.default_skip = 0
        self.default_limit = 10

    ## TEST CASES
    ## <CREATE_AGENT>
    def test_create_agent_success(self):
        """
        Test successful creation of an agent.
        """
        agent_create = AgentCreate(name=self.default_agent_name, role_id=self.default_role_id)
        self.mock_db.add = MagicMock()
        self.mock_db.commit = MagicMock()
        self.mock_db.refresh = MagicMock(return_value=None)

        created_agent = self.agent_service.create_agent(agent=agent_create)
        self.assertIsNotNone(created_agent)
        self.mock_db.add.assert_called_once()
        self.mock_db.commit.assert_called_once()
        self.mock_db.refresh.assert_called_once_with(created_agent)

    def test_create_agent_failure(self):
        """
        Test failure in creating an agent due to a database error.
        """
        agent_create = AgentCreate(name=self.default_agent_name, role_id=self.default_role_id)
        self.mock_db.add = MagicMock()
        self.mock_db.commit = MagicMock(side_effect=Exception("DB commit failed"))
        self.mock_db.rollback = MagicMock()

        with self.assertRaises(Exception):
            self.agent_service.create_agent(agent=agent_create)
        self.mock_db.rollback.assert_called_once()

    ## <GET_AGENTS>
    def test_get_agents_success(self):
        """
        Test successful retrieval of agents.
        """
        self.mock_db.query.return_value.offset.return_value.limit.return_value.all.return_value = [
            SchemaAgent(id=self.default_agent_id, name=self.default_agent_name, role_id=self.default_role_id)
        ]

        agents = self.agent_service.get_agents(skip=self.default_skip, limit=self.default_limit)
        self.assertIsInstance(agents, list)
        self.assertGreaterEqual(len(agents), 1)

    ## <GET_AGENT>
    def test_get_agent_success(self):
        """
        Test successful retrieval of a single agent by ID.
        """
        self.mock_db.query.return_value.filter.return_value.first.return_value = SchemaAgent(id=self.default_agent_id, name=self.default_agent_name, role_id=self.default_role_id)

        agent = self.agent_service.get_agent(agent_id=self.default_agent_id)
        self.assertIsNotNone(agent)
        self.assertEqual(agent.id, self.default_agent_id)

    def test_get_agent_not_found(self):
        """
        Test retrieval of a non-existing agent.
        """
        self.mock_db.query.return_value.filter.return_value.first.return_value = None

        agent = self.agent_service.get_agent(agent_id=self.default_agent_id)
        self.assertIsNone(agent)

    ## <UPDATE_AGENT>
    def test_update_agent_success(self):
        """
        Test successful update of an agent's information.
        """
        agent_create = AgentCreate(name="Updated Agent", role_id=self.default_role_id)
        self.mock_db.query.return_value.filter.return_value.first.return_value = SchemaAgent(id=self.default_agent_id, name=self.default_agent_name, role_id=self.default_role_id)
        self.mock_db.commit = MagicMock()
        self.mock_db.refresh = MagicMock()

        updated_agent = self.agent_service.update_agent(agent_id=self.default_agent_id, agent=agent_create)
        self.assertIsNotNone(updated_agent)
        self.assertEqual(updated_agent.name, "Updated Agent")

    def test_update_agent_not_found(self):
        """
        Test update attempt on a non-existing agent.
        """
        agent_create = AgentCreate(name="Updated Agent", role_id=self.default_role_id)
        self.mock_db.query.return_value.filter.return_value.first.return_value = None

        updated_agent = self.agent_service.update_agent(agent_id=self.default_agent_id, agent=agent_create)
        self.assertIsNone(updated_agent)

    ## <DELETE_AGENT>
    def test_delete_agent_success(self):
        """
        Test successful deletion of an agent.
        """
        self.mock_db.query.return_value.filter.return_value.first.return_value = SchemaAgent(id=self.default_agent_id, name=self.default_agent_name, role_id=self.default_role_id)
        self.mock_db.delete = MagicMock()
        self.mock_db.commit = MagicMock()

        deleted_agent = self.agent_service.delete_agent(agent_id=self.default_agent_id)
        self.assertIsNotNone(deleted_agent)

    def test_delete_agent_not_found(self):
        """
        Test deletion attempt on a non-existing agent.
        """
        self.mock_db.query.return_value.filter.return_value.first.return_value = None

        deleted_agent = self.agent_service.delete_agent(agent_id=self.default_agent_id)
        self.assertIsNone(deleted_agent)

if __name__ == '__main__':
    unittest.main()
