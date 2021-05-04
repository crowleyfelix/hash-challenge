import logging

from pydantic import BaseModel
from .discount import Discount

logger = logging.getLogger(__name__)

class Product(BaseModel):
    id: str = None
    price_in_cents: int = None
    title: str = None
    description: str = None
    _discount = None

    @property
    def discount(self):
        logger.info("Calculating discount")
        return Discount(percentage=0.1, value_in_cents=234)