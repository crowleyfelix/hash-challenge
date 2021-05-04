from pydantic import BaseModel


class BaseError(Exception):
    message: str = "Internal error ocurred"
    status_code: int = 500

    def __init__(self, message=None, status_code=None):
        self.message = message or self.message
        self.status_code = status_code or self.status_code
        super().__init__(message)

    def dict(self):
        return {
            "message": self.message
        }


class NotFound(BaseError):
    message = "Not found"
    status_code = 404
