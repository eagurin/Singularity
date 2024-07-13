"""
## IMPORTS
"""
import unittest
from unittest.mock import patch

## REQUIREMENTS
# This test suite requires the following Python packages to be installed:
# - fastapi
# - sqlalchemy
# - pytest
# You can install them using pip:
# pip install fastapi sqlalchemy pytest

try:
    from fastapi.testclient import TestClient
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from app.main import app
    from app.db.session import Base
except ImportError as e:
    raise ImportError("Some required modules are missing. Please ensure to install 'fastapi', 'sqlalchemy', and 'pytest'.") from e

"""
## SETUP
"""
class TestMain(unittest.TestCase):
    def setUp(self):
        # Setup test client and in-memory database for testing
        self.client = TestClient(app)
        self.engine = create_engine("sqlite:///:memory:")
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.db = SessionLocal()
        Base.metadata.create_all(bind=self.engine)

    def tearDown(self):
        # Clean up the database after each test
        Base.metadata.drop_all(bind=self.engine)

    """
    ## DATABASE STARTUP EVENT
    """
    def test_startup_event(self):
        # Mock the engine and metadata.create_all to test startup event without affecting the actual database
        with patch("app.main.engine", self.engine):
            with patch("app.models.database.agent.Base.metadata.create_all") as agent_mock, \
                 patch("app.models.database.role.Base.metadata.create_all") as role_mock, \
                 patch("app.models.database.influence.Base.metadata.create_all") as influence_mock, \
                 patch("app.models.database.task.Base.metadata.create_all") as task_mock, \
                 patch("app.models.database.group.Base.metadata.create_all") as group_mock, \
                 patch("app.models.database.news_model.Base.metadata.create_all") as news_mock, \
                 patch("app.models.database.recommendation.Base.metadata.create_all") as recommendation_mock, \
                 patch("app.models.database.training_model.Base.metadata.create_all") as training_mock, \
                 patch("app.models.database.feedback_model.Base.metadata.create_all") as feedback_mock:
                app.trigger_event("startup")
                agent_mock.assert_called_once()
                role_mock.assert_called_once()
                influence_mock.assert_called_once()
                task_mock.assert_called_once()
                group_mock.assert_called_once()
                news_mock.assert_called_once()
                recommendation_mock.assert_called_once()
                training_mock.assert_called_once()
                feedback_mock.assert_called_once()

    """
    ## DATABASE SHUTDOWN EVENT
    """
    def test_shutdown_event(self):
        # Mock the SessionLocal.close to test shutdown event
        with patch("app.db.session.SessionLocal.close") as mock_close:
            app.trigger_event("shutdown")
            mock_close.assert_called()

    """
    ## DEPENDENCY INJECTION
    """
    def test_get_db_dependency(self):
        # Test the get_db dependency to ensure it provides a session from the mocked database
        with patch("app.main.get_db", return_value=self.db) as mock_session:
            db = next(app.dependency_overrides[app.get_db]())
            self.assertEqual(db, self.db)
            mock_session.assert_called_once()

    """
    ## ROUTES INCLUSION
    """
    def test_routes_inclusion(self):
        # Test each route to ensure they are included and accessible
        routes = [
            "/api/v1/agents",
            "/api/v1/roles",
            "/api/v1/influences",
            "/api/v1/stages",
            "/api/v1/groups",
            "/api/v1/tasks",
            "/api/v1/news",
            "/api/v1/recommendations",
            "/api/v1/training",
            "/api/v1/feedback",
        ]
        for route in routes:
            response = self.client.get(route)
            self.assertNotEqual(response.status_code, 404, f"Route {route} should not return 404")

if __name__ == "__main__":
    unittest.main()
