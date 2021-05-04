import logging
from app.infrastructure import ioc

logger = logging.getLogger(__name__)

class ProductService:
    async def list(self, filters):
        logger.info(f"Listing products by filters {filters}")
        repo = ioc.instance(ioc.Dependencies.product_repo)
        return await repo.list(filters)