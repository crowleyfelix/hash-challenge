from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    id: str = None
    first_name:   str = None
    last_name:    str = None
    date_of_birth: datetime = None
