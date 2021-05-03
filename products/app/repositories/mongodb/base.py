from motor.core import Collection
from .schemas import BaseSchema

class BaseRepository:
    collection_name = None
    search_schema: BaseSchema = None
    entity_schema: BaseSchema = None

    def __init__(self, database):

        if not self.collection_name:
            raise NotImplementedError("The collection name wasn't set")

        self.collection: Collection = database[self.collection_name]
        super().__init__()


    async def _list(self, filters: dict):
        query = self.search_schema.dump(filters)

        limit = "limit" in query and query.pop("limit")
        offset = "offset" in query and query.pop("offset")

        for key, value in query.items():
            if isinstance(value, list):
                query[key] = {"$in": value}

        cursor = self.collection.find(query)

        if limit is not None and offset is not None:
            cursor = cursor.skip(offset).limit(limit)

        items = []
        async for item in cursor:
            items.append(self.entity_schema.load(item))

        return items