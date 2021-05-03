from .base import BaseRepository
from .schemas import PAGING_SCHEMA, PRODUCT_SCHEMA

class ProductRepository(BaseRepository):
    collection_name = "products"
    entity_schema = PRODUCT_SCHEMA
    search_schema = PAGING_SCHEMA

    async def list(self, filters: dict):
        return await self._list(filters)
            


