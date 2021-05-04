import logging
from app import domain
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

        for pr in products:
            pr.discount_calculator = calculator

        return contracts.ListProductsResponse(data=products, **request)
