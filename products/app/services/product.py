from app.infrastructure import ioc

class ProductService:
    def list(self, filters):
        repo = ioc.instance(ioc.Dependencies.product_repo)
        return await repo.list(filters)