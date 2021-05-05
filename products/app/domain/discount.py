import logging
from pydantic import BaseModel
from proto.discounts_pb2 import CalculateRequest, CalculateResponse
from app.infrastructure import ioc
from .user import User

logger = logging.getLogger(__name__)


class Discount(BaseModel):
    percentage: float = None
    value_in_cents: int = None


class DiscountCalculator(BaseModel):
    user: User = None

    async def calculate(self, product):
        logger.info("Calculating discount")
        calculator = ioc.instance(ioc.Dependencies.discounts_api)

        request = CalculateRequest()
        request.user_id = self.user.id
        request.product_id = product.id

        resp: CalculateResponse = await calculator.Calculate(request)
        discount = resp.product.discount

        if discount and discount.percentage > 0:
            return Discount(percentage=discount.percentage, value_in_cents=discount.value_in_cents)
