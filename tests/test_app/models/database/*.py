## test_app/models/database/test_models.py
"""
This test module is designed to verify the correctness and robustness of the database models
defined in the app/models/database/*.py file. It uses Python's unittest framework to create
a comprehensive test suite that covers various aspects of the models, including relationships,
constraints, and table properties.
"""

import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from app.models.database import Base, Agent, Role, Influence, Task, Group, News, Recommendation, Training, Feedback

## SETUP
class TestDatabaseModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up a temporary in-memory database before any tests are run.
        """
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    @classmethod
    def tearDownClass(cls):
        """
        Ensure the database is discarded after tests are done.
        """
        Base.metadata.drop_all(cls.engine)

    def setUp(self):
        """
        Create a new database session for a test.
        """
        self.session = self.Session()

    def tearDown(self):
        """
        Rollback and close the session after a test.
        """
        self.session.rollback()
        self.session.close()

## TEST CASES
    ## <TEST_AGENT_ROLE_RELATIONSHIP>
    def test_agent_role_relationship(self):
        """
        Test the relationship between Agent and Role models.
        """
        role = Role(name="Test Role")
        agent = Agent(name="Test Agent", role=role)
        self.session.add(role)
        self.session.add(agent)
        self.session.commit()

        self.assertEqual(agent.role.name, "Test Role")
        self.assertIn(agent, role.agents)

    ## <TEST_TASK_AGENT_RELATIONSHIP>
    def test_task_agent_relationship(self):
        """
        Test the relationship between Task and Agent models.
        """
        agent = Agent(name="Test Agent")
        task = Task(description="Test Task", agent=agent)
        self.session.add(agent)
        self.session.add(task)
        self.session.commit()

        self.assertEqual(task.agent.name, "Test Agent")
        self.assertIn(task, agent.tasks)

    ## <TEST_GROUP_TASKS_RELATIONSHIP>
    def test_group_tasks_relationship(self):
        """
        Test the many-to-many relationship between Group and Task models.
        """
        group = Group(name="Test Group")
        task1 = Task(description="Test Task 1")
        task2 = Task(description="Test Task 2")
        group.tasks.append(task1)
        group.tasks.append(task2)
        self.session.add(group)
        self.session.commit()

        self.assertIn(task1, group.tasks)
        self.assertIn(task2, group.tasks)
        self.assertEqual(len(group.tasks), 2)

    ## <TEST_UNIQUE_CONSTRAINTS>
    def test_unique_constraints(self):
        """
        Test that unique constraints on certain fields are enforced.
        """
        role1 = Role(name="Unique Role")
        role2 = Role(name="Unique Role")
        self.session.add(role1)
        self.session.commit()
        with self.assertRaises(Exception):
            self.session.add(role2)
            self.session.commit()

    ## <TEST_STRING_FIELDS>
    def test_string_fields(self):
        """
        Test that string fields store and retrieve correctly.
        """
        news = News(title="Test News", content="This is a test news content.")
        self.session.add(news)
        self.session.commit()

        retrieved_news = self.session.query(News).first()
        self.assertEqual(retrieved_news.title, "Test News")
        self.assertEqual(retrieved_news.content, "This is a test news content.")

if __name__ == '__main__':
    unittest.main()
