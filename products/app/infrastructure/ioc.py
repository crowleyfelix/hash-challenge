import inject


class Dependencies:
    config = "config"
    loop = "loop"
    product_repo = "product_repo"
    product_svc = "product_svc"
    mongodb_driver = "mongodb_driver"


def configure(binder):
    inject.configure(binder, False)


def instance(key: Dependencies):
    return inject.instance(key)

async def dispose(self):
    inject.clear()
