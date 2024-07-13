## app/middleware/error_handler.py

from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging

# Initialize logger
logger = logging.getLogger("app.middleware.error_handler")

def add_error_handlers(app: FastAPI):
    """
    Function to add custom error handlers to the FastAPI app.

    Args:
        app (FastAPI): The FastAPI application instance.
    """

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        """
        Handle HTTP exceptions.

        Args:
            request (Request): The request instance.
            exc (StarletteHTTPException): The HTTP exception instance.

        Returns:
            JSONResponse: The JSON response with error details.
        """
        logger.error(f"HTTP error occurred: {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """
        Handle request validation errors.

        Args:
            request (Request): The request instance.
            exc (RequestValidationError): The validation error instance.

        Returns:
            JSONResponse: The JSON response with error details.
        """
        logger.error(f"Validation error occurred: {exc.errors()}")
        return JSONResponse(
            status_code=422,
            content={"detail": exc.errors()},
        )

    @app.exception_handler(SQLAlchemyError)
    async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
        """
        Handle SQLAlchemy errors.

        Args:
            request (Request): The request instance.
            exc (SQLAlchemyError): The SQLAlchemy error instance.

        Returns:
            JSONResponse: The JSON response with error details.
        """
        logger.error(f"Database error occurred: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={"detail": "A database error occurred."},
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        """
        Handle general exceptions.

        Args:
            request (Request): The request instance.
            exc (Exception): The general exception instance.

        Returns:
            JSONResponse: The JSON response with error details.
        """
        logger.error(f"An error occurred: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={"detail": "An internal server error occurred."},
        )
