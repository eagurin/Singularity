## app/middleware/error_handler.py
import logging

from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from transformers import TranslationPipeline


def setup_error_handlers(app):

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        """
        Handles HTTP exceptions, returning a JSON response with the error details.
        """
        return JSONResponse(
            status_code=exc.status_code, content={"detail": exc.detail}
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        """
        Handles request validation errors, returning a JSON response with the error details.
        """
        return JSONResponse(status_code=422, content={"detail": exc.errors()})

    @app.exception_handler(SQLAlchemyError)
    async def sqlalchemy_exception_handler(
        request: Request, exc: SQLAlchemyError
    ):
        """
        Handles SQLAlchemy errors, logging the error and returning a generic error response.
        """
        logging.error(f"Database error occurred: {exc}")
        return JSONResponse(
            status_code=500,
            content={"detail": "An internal server error occurred"},
        )

    @app.exception_handler(TranslationPipeline)
    async def translation_pipeline_exception_handler(
        request: Request, exc: TranslationPipeline
    ):
        """
        Handles errors from the TranslationPipeline, logging the error and returning a specific error response.
        """
        logging.error(f"Translation pipeline error occurred: {exc}")
        return JSONResponse(
            status_code=500, content={"detail": "A translation error occurred"}
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        """
        Handles all uncaught exceptions, logging the error and returning a generic error response.
        """
        logging.error(f"Unhandled exception occurred: {exc}")
        return JSONResponse(
            status_code=500,
            content={"detail": "An internal server error occurred"},
        )
