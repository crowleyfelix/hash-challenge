from typing import Any, List
from pydantic import BaseModel
from app import domain, errors


class ListRequest(BaseModel):
    limit: int = 10
    offset: int = 0


class Response(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    data: Any = None
    error: errors.BaseError = None


class ListResponse(Response, ListRequest):
    pass


class ListProductsRequest(ListRequest):
    user_id: str = None


class ListProductsResponse(ListResponse):
    pass
