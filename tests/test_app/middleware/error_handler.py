## test_app/middleware/error_handler.py
"""
This module contains the test cases for error_handler.py in the async_fastapi_nlp_agent_system.
"""

import unittest
from unittest.mock import AsyncMock, patch
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
from transformers import TranslationPipeline
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY, HTTP_500_INTERNAL_SERVER_ERROR

## Import the setup_error_handlers function from the actual location
from app.middleware.error_handler import setup_error_handlers

class TestErrorHandler(unittest.TestCase):

    ## SETUP
    def setUp(self) -> None:
        self.app = FastAPI()
        setup_error_handlers(self.app)
        self.request = Request(scope={"type": "http"})

    ## HTTP EXCEPTION HANDLER TEST
    @patch("fastapi.responses.JSONResponse")
    async def test_http_exception_handler(self, mock_json_response):
        """
        Test the HTTP exception handler.
        """
        exc = HTTPException(status_code=404, detail="Not found")
        response = await self.app.exception_handlers[HTTPException](self.request, exc)
        mock_json_response.assert_called_once_with(
            status_code=404,
            content={"detail": "Not found"}
        )

    ## VALIDATION EXCEPTION HANDLER TEST
    @patch("fastapi.responses.JSONResponse")
    async def test_validation_exception_handler(self, mock_json_response):
        """
        Test the request validation exception handler.
        """
        exc = RequestValidationError(errors=[{"msg": "Invalid field"}])
        response = await self.app.exception_handlers[RequestValidationError](self.request, exc)
        mock_json_response.assert_called_once_with(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": exc.errors()}
        )

    ## SQLALCHEMY EXCEPTION HANDLER TEST
    @patch("logging.error")
    @patch("fastapi.responses.JSONResponse")
    async def test_sqlalchemy_exception_handler(self, mock_json_response, mock_logging_error):
        """
        Test the SQLAlchemy exception handler.
        """
        exc = SQLAlchemyError("Database error")
        response = await self.app.exception_handlers[SQLAlchemyError](self.request, exc)
        mock_logging_error.assert_called_once_with(f"Database error occurred: {exc}")
        mock_json_response.assert_called_once_with(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "An internal server error occurred"}
        )

    ## TRANSLATION PIPELINE EXCEPTION HANDLER TEST
    @patch("logging.error")
    @patch("fastapi.responses.JSONResponse")
    async def test_translation_pipeline_exception_handler(self, mock_json_response, mock_logging_error):
        """
        Test the TranslationPipeline exception handler.
        """
        exc = TranslationPipeline("Translation error")
        response = await self.app.exception_handlers[TranslationPipeline](self.request, exc)
        mock_logging_error.assert_called_once_with(f"Translation pipeline error occurred: {exc}")
        mock_json_response.assert_called_once_with(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "A translation error occurred"}
        )

    ## GENERIC EXCEPTION HANDLER TEST
    @patch("logging.error")
    @patch("fastapi.responses.JSONResponse")
    async def test_generic_exception_handler(self, mock_json_response, mock_logging_error):
        """
        Test the generic exception handler.
        """
        exc = Exception("Unexpected error")
        response = await self.app.exception_handlers[Exception](self.request, exc)
        mock_logging_error.assert_called_once_with(f"Unhandled exception occurred: {exc}")
        mock_json_response.assert_called_once_with(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "An internal server error occurred"}
        )

if __name__ == "__main__":
    unittest.main()
