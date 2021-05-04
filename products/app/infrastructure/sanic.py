import logging
from sanic import json, exceptions
from sanic.handlers import ErrorHandler
from app import errors


class CustomErrorHandler(ErrorHandler):
    def default(self, request, exception):
        logger = logging.getLogger(__name__)

        if isinstance(exception, exceptions.SanicException):
            exception = errors.BaseError(message=str(exception), status_code=exception.status_code)

        elif not isinstance(exception, errors.BaseError):
            logger.error(f"Unexpected failure", exception)
            exception = errors.BaseError()

        return json(exception.dict(), status=exception.status_code)
