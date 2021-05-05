import logging

from pydantic import BaseModel, PrivateAttr
from .discount import Discount, DiscountCalculator

logger = logging.getLogger(__name__)


class Product(BaseModel):
    id: str = None
    price_in_cents: int = None
    title: str = None
    description: str = None
    discount: Discount = None
