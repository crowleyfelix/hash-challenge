import logging
from pydantic import BaseModel
from proto.discounts_pb2 import CalculateRequest
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

        resp = await calculator.Calculate(request)
        return Discount(percentage=0.1, value_in_cents=234)
