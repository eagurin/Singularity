"""
## test_app/models/database/test_models.py
"""

import unittest

try:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    from app.models.database.base import Base
    from app.models.database.agent import Agent
    from app.models.database.role import Role
    from app.models.database.influence import Influence
    from app.models.database.task import Task
    from app.models.database.group import Group
    from app.models.database.news import News
    from app.models.database.recommendation import Recommendation
    from app.models.database.training import Training
    from app.models.database.feedback import Feedback
except ModuleNotFoundError:
    import sys
    print("Required module 'sqlalchemy' not found. Please install it using pip.")
    sys.exit(1)


class TestDatabaseModels(unittest.TestCase):
    """
    ## SETUP AND TEARDOWN
    """
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        Base.metadata.drop_all(cls.engine)

    """
    ## AGENT MODEL TESTS
    """
    def test_create_agent(self):
        new_agent = Agent(name="Test Agent", role_id=1)
        self.session.add(new_agent)
        self.session.commit()
        query_agent = self.session.query(Agent).filter_by(name="Test Agent").first()
        self.assertIsNotNone(query_agent)
        self.assertEqual(query_agent.name, "Test Agent")

    """
    ## ROLE MODEL TESTS
    """
    def test_create_role(self):
        new_role = Role(name="Test Role")
        self.session.add(new_role)
        self.session.commit()
        query_role = self.session.query(Role).filter_by(name="Test Role").first()
        self.assertIsNotNone(query_role)
        self.assertEqual(query_role.name, "Test Role")

    """
    ## INFLUENCE MODEL TESTS
    """
    def test_create_influence(self):
        new_influence = Influence(name="Test Influence")
        self.session.add(new_influence)
        self.session.commit()
        query_influence = self.session.query(Influence).filter_by(name="Test Influence").first()
        self.assertIsNotNone(query_influence)
        self.assertEqual(query_influence.name, "Test Influence")

    """
    ## TASK MODEL TESTS
    """
    def test_create_task(self):
        new_task = Task(description="Test Task", agent_id=1)
        self.session.add(new_task)
        self.session.commit()
        query_task = self.session.query(Task).filter_by(description="Test Task").first()
        self.assertIsNotNone(query_task)
        self.assertEqual(query_task.description, "Test Task")

    """
    ## GROUP MODEL TESTS
    """
    def test_create_group(self):
        new_group = Group(name="Test Group")
        self.session.add(new_group)
        self.session.commit()
        query_group = self.session.query(Group).filter_by(name="Test Group").first()
        self.assertIsNotNone(query_group)
        self.assertEqual(query_group.name, "Test Group")

    """
    ## NEWS MODEL TESTS
    """
    def test_create_news(self):
        new_news = News(title="Test News", content="Test Content")
        self.session.add(new_news)
        self.session.commit()
        query_news = self.session.query(News).filter_by(title="Test News").first()
        self.assertIsNotNone(query_news)
        self.assertEqual(query_news.title, "Test News")
        self.assertEqual(query_news.content, "Test Content")

    """
    ## RECOMMENDATION MODEL TESTS
    """
    def test_create_recommendation(self):
        new_recommendation = Recommendation(title="Test Recommendation", content="Test Content")
        self.session.add(new_recommendation)
        self.session.commit()
        query_recommendation = self.session.query(Recommendation).filter_by(title="Test Recommendation").first()
        self.assertIsNotNone(query_recommendation)
        self.assertEqual(query_recommendation.title, "Test Recommendation")
        self.assertEqual(query_recommendation.content, "Test Content")

    """
    ## TRAINING MODEL TESTS
    """
    def test_create_training(self):
        new_training = Training(title="Test Training", content="Test Content")
        self.session.add(new_training)
        self.session.commit()
        query_training = self.session.query(Training).filter_by(title="Test Training").first()
        self.assertIsNotNone(query_training)
        self.assertEqual(query_training.title, "Test Training")
        self.assertEqual(query_training.content, "Test Content")

    """
    ## FEEDBACK MODEL TESTS
    """
    def test_create_feedback(self):
        new_feedback = Feedback(content="Test Feedback")
        self.session.add(new_feedback)
        self.session.commit()
        query_feedback = self.session.query(Feedback).filter_by(content="Test Feedback").first()
        self.assertIsNotNone(query_feedback)
        self.assertEqual(query_feedback.content, "Test Feedback")


if __name__ == '__main__':
    unittest.main()
