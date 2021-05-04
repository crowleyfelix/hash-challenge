from pydantic import BaseModel


class Discount(BaseModel):
    percentage: float = None
    value_in_cents: str = None
