## test_app/db/session.py
"""
This module contains tests for the app/db/session.py module.
"""

import unittest
from unittest.mock import patch, MagicMock
from sqlalchemy.orm import Session
from app.db.session import get_db

## TestSettings
class TestSettings:
    DATABASE_URL = "sqlite:///./test.db"

## TestSession
class TestSession(unittest.TestCase):

    @patch("app.db.session.settings", new=TestSettings())
    @patch("app.db.session.SessionLocal")
    def test_get_db(self, mock_session_local):
        """
        Test the get_db generator function to ensure it yields a database session and closes it properly.
        """
        # Mock the SessionLocal to return a mock session when called
        mock_session = MagicMock(spec=Session)
        mock_session_local.return_value = mock_session

        # Call the get_db function and enter its context
        db_gen = get_db()
        db_session = next(db_gen)

        # Verify the yielded object is the mock session
        self.assertIs(db_session, mock_session)

        # Verify closing the session
        with self.assertRaises(StopIteration):
            next(db_gen)
        mock_session.close.assert_called_once()

## Main
if __name__ == "__main__":
    unittest.main()
