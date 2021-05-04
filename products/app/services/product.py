import logging
from app import domain
from app.infrastructure import ioc

logger = logging.getLogger(__name__)

class ProductService:
    async def list(self, user_id, filters):
        logger.info(f"Listing products by filters {filters}")
        user = domain.User(id=user_id)
        calculator = domain.DiscountCalculator(user=user)

        repo = ioc.instance(ioc.Dependencies.product_repo)
        products = await repo.list(filters)

        for pr in products:
            pr.discount_calculator = calculator

        return products   