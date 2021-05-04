import logging

from pydantic import BaseModel, PrivateAttr
from .discount import Discount, DiscountCalculator

logger = logging.getLogger(__name__)


class Product(BaseModel):
    id: str = None
    price_in_cents: int = None
    title: str = None
    description: str = None
    discount_calculator: DiscountCalculator = None
    _discount: Discount = PrivateAttr(default=None)

    @property
    def discount(self):
        if not self._discount:
            self._discount = self.discount_calculator.calculate()

        return self._discount

    def dict(self):
        d = super().dict()
        d["discount"] = self.discount and self.discount.dict()
        return d