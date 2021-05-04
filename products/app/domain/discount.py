import logging
from pydantic import BaseModel
from .user import User

logger = logging.getLogger(__name__)

class Discount(BaseModel):
    percentage: float = None
    value_in_cents: int = None


class DiscountCalculator(BaseModel):
    user: User = None

    def calculate(self):
        logger.info("Calculating discount")
        return Discount(percentage=0.1, value_in_cents=234)
