## test_app/models/schemas/test_schemas.py
"""
This test module covers the test cases for the schemas defined in the app/models/schemas directory.
It uses Python's unittest framework to ensure the correctness and robustness of the code.
"""

import unittest
from pydantic import ValidationError
from app.models.schemas.agent import Agent, AgentCreate
from app.models.schemas.role import Role, RoleCreate
from app.models.schemas.influence import Influence, InfluenceCreate
from app.models.schemas.task import Task, TaskCreate
from app.models.schemas.group import Group, GroupCreate
from app.models.schemas.news import News, NewsCreate
from app.models.schemas.recommendation import Recommendation, RecommendationCreate
from app.models.schemas.training import Training, TrainingCreate
from app.models.schemas.feedback import Feedback, FeedbackCreate

## TestAgentSchema
class TestAgentSchema(unittest.TestCase):
    def test_create_agent_with_minimum_fields(self):
        agent = AgentCreate(name="John Doe")
        self.assertEqual(agent.name, "John Doe")
        self.assertIsNone(agent.role_id)

    def test_create_agent_with_all_fields(self):
        agent = Agent(id=1, name="John Doe", role_id=2)
        self.assertEqual(agent.id, 1)
        self.assertEqual(agent.name, "John Doe")
        self.assertEqual(agent.role_id, 2)

    def test_agent_with_invalid_field(self):
        with self.assertRaises(ValidationError):
            Agent(id="one", name="John Doe", role_id="two")

## TestRoleSchema
class TestRoleSchema(unittest.TestCase):
    def test_create_role_with_minimum_fields(self):
        role = RoleCreate(name="Administrator")
        self.assertEqual(role.name, "Administrator")

    def test_create_role_with_all_fields(self):
        role = Role(id=1, name="Administrator")
        self.assertEqual(role.id, 1)
        self.assertEqual(role.name, "Administrator")

    def test_role_with_invalid_field(self):
        with self.assertRaises(ValidationError):
            Role(id="one", name=123)

## TestInfluenceSchema
class TestInfluenceSchema(unittest.TestCase):
    def test_create_influence_with_minimum_fields(self):
        influence = InfluenceCreate(name="Positive")
        self.assertEqual(influence.name, "Positive")

    def test_create_influence_with_all_fields(self):
        influence = Influence(id=1, name="Positive")
        self.assertEqual(influence.id, 1)
        self.assertEqual(influence.name, "Positive")

    def test_influence_with_invalid_field(self):
        with self.assertRaises(ValidationError):
            Influence(id="one", name=123)

## TestTaskSchema
class TestTaskSchema(unittest.TestCase):
    def test_create_task_with_minimum_fields(self):
        task = TaskCreate(description="Complete the project documentation.")
        self.assertEqual(task.description, "Complete the project documentation.")

    def test_create_task_with_all_fields(self):
        task = Task(id=1, description="Complete the project documentation.", agent_id=2)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Complete the project documentation.")
        self.assertEqual(task.agent_id, 2)

    def test_task_with_invalid_field(self):
        with self.assertRaises(ValidationError):
            Task(id="one", description=123, agent_id="two")

## TestGroupSchema
class TestGroupSchema(unittest.TestCase):
    def test_create_group_with_minimum_fields(self):
        group = GroupCreate(name="Development Team")
        self.assertEqual(group.name, "Development Team")

    def test_create_group_with_all_fields(self):
        group = Group(id=1, name="Development Team", tasks=[])
        self.assertEqual(group.id, 1)
        self.assertEqual(group.name, "Development Team")
        self.assertEqual(group.tasks, [])

    def test_group_with_invalid_field(self):
        with self.assertRaises(ValidationError):
            Group(id="one", name=123, tasks="not a list")

## TestNewsSchema
class TestNewsSchema(unittest.TestCase):
    def test_create_news_with_minimum_fields(self):
        news = NewsCreate(title="New Feature Release", content="We are excited to announce the release of...")
        self.assertEqual(news.title, "New Feature Release")
        self.assertEqual(news.content, "We are excited to announce the release of...")

    def test_create_news_with_all_fields(self):
        news = News(id=1, title="New Feature Release", content="We are excited to announce the release of...")
        self.assertEqual(news.id, 1)
        self.assertEqual(news.title, "New Feature Release")
        self.assertEqual(news.content, "We are excited to announce the release of...")

    def test_news_with_invalid_field(self):
        with self.assertRaises(ValidationError):
            News(id="one", title=123, content=456)

## TestRecommendationSchema
class TestRecommendationSchema(unittest.TestCase):
    def test_create_recommendation_with_minimum_fields(self):
        recommendation = RecommendationCreate(title="Recommended Practices for Security", content="It is recommended to regularly update your passwords...")
        self.assertEqual(recommendation.title, "Recommended Practices for Security")
        self.assertEqual(recommendation.content, "It is recommended to regularly update your passwords...")

    def test_create_recommendation_with_all_fields(self):
        recommendation = Recommendation(id=1, title="Recommended Practices for Security", content="It is recommended to regularly update your passwords...")
        self.assertEqual(recommendation.id, 1)
        self.assertEqual(recommendation.title, "Recommended Practices for Security")
        self.assertEqual(recommendation.content, "It is recommended to regularly update your passwords...")

    def test_recommendation_with_invalid_field(self):
        with self.assertRaises(ValidationError):
            Recommendation(id="one", title=123, content=456)

## TestTrainingSchema
class TestTrainingSchema(unittest.TestCase):
    def test_create_training_with_minimum_fields(self):
        training = TrainingCreate(title="Docker Basics", content="Docker is a set of platform as a service products that use OS-level virtualization...")
        self.assertEqual(training.title, "Docker Basics")
        self.assertEqual(training.content, "Docker is a set of platform as a service products that use OS-level virtualization...")

    def test_create_training_with_all_fields(self):
        training = Training(id=1, title="Docker Basics", content="Docker is a set of platform as a service products that use OS-level virtualization...")
        self.assertEqual(training.id, 1)
        self.assertEqual(training.title, "Docker Basics")
        self.assertEqual(training.content, "Docker is a set of platform as a service products that use OS-level virtualization...")

    def test_training_with_invalid_field(self):
        with self.assertRaises(ValidationError):
            Training(id="one", title=123, content=456)

## TestFeedbackSchema
class TestFeedbackSchema(unittest.TestCase):
    def test_create_feedback_with_minimum_fields(self):
        feedback = FeedbackCreate(content="This new feature has significantly improved my workflow!")
        self.assertEqual(feedback.content, "This new feature has significantly improved my workflow!")

    def test_create_feedback_with_all_fields(self):
        feedback = Feedback(id=1, content="This new feature has significantly improved my workflow!")
        self.assertEqual(feedback.id, 1)
        self.assertEqual(feedback.content, "This new feature has significantly improved my workflow!")

    def test_feedback_with_invalid_field(self):
        with self.assertRaises(ValidationError):
            Feedback(id="one", content=123)

if __name__ == '__main__':
    unittest.main()
