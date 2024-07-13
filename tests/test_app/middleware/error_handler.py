## test_app/middleware/error_handler.py
"""
This module contains the test cases for error_handler.py in the app/middleware directory.
"""

import unittest
from unittest.mock import patch, MagicMock
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi.exceptions import RequestValidationError, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from app.middleware.error_handler import setup_error_handlers
from starlette.testclient import TestClient

## SETUP
class TestErrorHandler(unittest.TestCase):
    def setUp(self):
        """
        Setup test environment for error handlers.
        """
        self.app = FastAPI()
        setup_error_handlers(self.app)
        self.client = TestClient(self.app)

## HTTP EXCEPTION HANDLER TESTS
    @patch('fastapi.responses.JSONResponse')
    def test_http_exception_handler(self, mock_json_response):
        """
        Test the HTTP exception handler returns the correct JSON response.
        """
        request = Request(scope={"type": "http"})
        exc = HTTPException(status_code=404, detail="Not Found")
        response = self.client.app.exception_handlers[HTTPException](request, exc)
        mock_json_response.assert_called_once_with(
            status_code=404,
            content={"detail": "Not Found"}
        )

## VALIDATION EXCEPTION HANDLER TESTS
    @patch('fastapi.responses.JSONResponse')
    def test_validation_exception_handler(self, mock_json_response):
        """
        Test the request validation exception handler returns the correct JSON response.
        """
        request = Request(scope={"type": "http"})
        exc = RequestValidationError(errors=[{"msg": "Invalid field"}])
        response = self.client.app.exception_handlers[RequestValidationError](request, exc)
        mock_json_response.assert_called_once_with(
            status_code=422,
            content={"detail": exc.errors()}
        )

## SQLALCHEMY EXCEPTION HANDLER TESTS
    @patch('logging.error')
    @patch('fastapi.responses.JSONResponse')
    def test_sqlalchemy_exception_handler(self, mock_json_response, mock_logging_error):
        """
        Test the SQLAlchemy exception handler logs the error and returns the correct JSON response.
        """
        request = Request(scope={"type": "http"})
        exc = SQLAlchemyError("Database error")
        response = self.client.app.exception_handlers[SQLAlchemyError](request, exc)
        mock_logging_error.assert_called_once_with(f"Database error occurred: {exc}")
        mock_json_response.assert_called_once_with(
            status_code=500,
            content={"detail": "An internal server error occurred"}
        )

## GENERIC EXCEPTION HANDLER TESTS
    @patch('logging.error')
    @patch('fastapi.responses.JSONResponse')
    def test_generic_exception_handler(self, mock_json_response, mock_logging_error):
        """
        Test the generic exception handler logs the error and returns the correct JSON response.
        """
        request = Request(scope={"type": "http"})
        exc = Exception("Unexpected error")
        response = self.client.app.exception_handlers[Exception](request, exc)
        mock_logging_error.assert_called_once_with(f"Unhandled exception occurred: {exc}")
        mock_json_response.assert_called_once_with(
            status_code=500,
            content={"detail": "An internal server error occurred"}
        )

if __name__ == '__main__':
    unittest.main()
