## test_app/models/schemas/test_schemas.py
"""
This module contains the test cases for the schemas defined in app/models/schemas/*.py.
It uses Python's unittest framework to ensure the correctness and robustness of the code.
"""

import unittest
from datetime import datetime
from pydantic import ValidationError
from app.models.schemas import (
    SentimentAnalysisRequest,
    SentimentAnalysisResponse,
    EntityRecognitionRequest,
    EntityRecognitionResponse,
    LanguageTranslationRequest,
    LanguageTranslationResponse,
    Role,
    Agent,
    Task,
    Group,
    Influence,
    News,
    Recommendation,
    Training,
    Feedback,
)

## TestSentimentAnalysisSchemas
class TestSentimentAnalysisSchemas(unittest.TestCase):
    def test_sentiment_analysis_request(self):
        """Ensure SentimentAnalysisRequest schema works with valid data"""
        data = {"text": "I love sunny days but hate the rain."}
        request = SentimentAnalysisRequest(**data)
        self.assertEqual(request.text, data['text'])

    def test_sentiment_analysis_response(self):
        """Ensure SentimentAnalysisResponse schema works with valid data"""
        data = {"result": {"polarity": 0.1, "subjectivity": 0.3}}
        response = SentimentAnalysisResponse(result=data["result"])
        self.assertEqual(response.result, data["result"])

## TestEntityRecognitionSchemas
class TestEntityRecognitionSchemas(unittest.TestCase):
    def test_entity_recognition_request(self):
        """Ensure EntityRecognitionRequest schema works with valid data"""
        data = {"text": "London is a big city in the United Kingdom."}
        request = EntityRecognitionRequest(**data)
        self.assertEqual(request.text, data['text'])

    def test_entity_recognition_response(self):
        """Ensure EntityRecognitionResponse schema works with valid data"""
        data = {"entities": [{"entity": "London", "type": "Location"}]}
        response = EntityRecognitionResponse(entities=data["entities"])
        self.assertEqual(response.entities, data["entities"])

## TestLanguageTranslationSchemas
class TestLanguageTranslationSchemas(unittest.TestCase):
    def test_language_translation_request(self):
        """Ensure LanguageTranslationRequest schema works with valid data"""
        data = {"text": "Hello, how are you?", "target_language": "es"}
        request = LanguageTranslationRequest(**data)
        self.assertEqual(request.text, data['text'])
        self.assertEqual(request.target_language, data['target_language'])

    def test_language_translation_response(self):
        """Ensure LanguageTranslationResponse schema works with valid data"""
        data = {"translated_text": "Hola, ¿cómo estás?"}
        response = LanguageTranslationResponse(translated_text=data["translated_text"])
        self.assertEqual(response.translated_text, data["translated_text"])

## TestRoleSchemas
class TestRoleSchemas(unittest.TestCase):
    def test_role_schema(self):
        """Ensure Role schema works with valid data"""
        data = {"id": 1, "name": "Administrator"}
        role = Role(**data)
        self.assertEqual(role.id, data['id'])
        self.assertEqual(role.name, data['name'])

## TestAgentSchemas
class TestAgentSchemas(unittest.TestCase):
    def test_agent_schema(self):
        """Ensure Agent schema works with valid data"""
        data = {"id": 1, "name": "John Doe", "role_id": 2}
        agent = Agent(**data)
        self.assertEqual(agent.id, data['id'])
        self.assertEqual(agent.name, data['name'])
        self.assertEqual(agent.role_id, data['role_id'])

## TestTaskSchemas
class TestTaskSchemas(unittest.TestCase):
    def test_task_schema(self):
        """Ensure Task schema works with valid data"""
        data = {"id": 1, "description": "Complete the project documentation.", "agent_id": 1}
        task = Task(**data)
        self.assertEqual(task.id, data['id'])
        self.assertEqual(task.description, data['description'])
        self.assertEqual(task.agent_id, data['agent_id'])

## TestGroupSchemas
class TestGroupSchemas(unittest.TestCase):
    def test_group_schema(self):
        """Ensure Group schema works with valid data"""
        data = {"id": 1, "name": "Development Team", "tasks": []}
        group = Group(**data)
        self.assertEqual(group.id, data['id'])
        self.assertEqual(group.name, data['name'])
        self.assertEqual(group.tasks, data['tasks'])

## TestInfluenceSchemas
class TestInfluenceSchemas(unittest.TestCase):
    def test_influence_schema(self):
        """Ensure Influence schema works with valid data"""
        data = {"id": 1, "name": "Positive"}
        influence = Influence(**data)
        self.assertEqual(influence.id, data['id'])
        self.assertEqual(influence.name, data['name'])

## TestNewsSchemas
class TestNewsSchemas(unittest.TestCase):
    def test_news_schema(self):
        """Ensure News schema works with valid data"""
        data = {"id": 1, "title": "New Feature Release", "content": "We are excited to announce the release of..."}
        news = News(**data)
        self.assertEqual(news.id, data['id'])
        self.assertEqual(news.title, data['title'])
        self.assertEqual(news.content, data['content'])

## TestRecommendationSchemas
class TestRecommendationSchemas(unittest.TestCase):
    def test_recommendation_schema(self):
        """Ensure Recommendation schema works with valid data"""
        data = {"id": 1, "title": "Recommended Practices for Security", "content": "It is recommended to regularly update your passwords..."}
        recommendation = Recommendation(**data)
        self.assertEqual(recommendation.id, data['id'])
        self.assertEqual(recommendation.title, data['title'])
        self.assertEqual(recommendation.content, data['content'])

## TestTrainingSchemas
class TestTrainingSchemas(unittest.TestCase):
    def test_training_schema(self):
        """Ensure Training schema works with valid data"""
        data = {"id": 1, "title": "Docker Basics", "content": "Docker is a set of platform as a service products that use OS-level virtualization..."}
        training = Training(**data)
        self.assertEqual(training.id, data['id'])
        self.assertEqual(training.title, data['title'])
        self.assertEqual(training.content, data['content'])

## TestFeedbackSchemas
class TestFeedbackSchemas(unittest.TestCase):
    def test_feedback_schema(self):
        """Ensure Feedback schema works with valid data"""
        data = {"id": 1, "content": "This new feature has significantly improved my workflow!"}
        feedback = Feedback(**data)
        self.assertEqual(feedback.id, data['id'])
        self.assertEqual(feedback.content, data['content'])

if __name__ == '__main__':
    unittest.main()
