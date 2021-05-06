import logging
import asyncio
from app import domain, errors
from app.infrastructure import ioc
from . import contracts

logger = logging.getLogger(__name__)


class ProductService:
    async def list(self, user_id, filters):
        logger.info(f"Listing products by filters {filters}")
        request = dict(contracts.ListProductsRequest(user_id=user_id, **filters))

        user = domain.User(id=user_id)
        calculator = domain.DiscountCalculator(user=user)

        repo = ioc.instance(ioc.Dependencies.product_repo)
        products = await repo.list(request)

        async def calculate_discount(product):
            try:
                product.discount = await calculator.calculate(product)
            except errors.BaseError:
                raise
            except Exception as ex:
                logger.warning(f"Failed calculating discount for product {product.id}: {ex}")

        await asyncio.gather(*[calculate_discount(pr) for pr in products])

        return contracts.ListProductsResponse(data=products, **request)
