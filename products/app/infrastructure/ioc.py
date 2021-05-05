from enum import Enum
import inject


class Dependencies(Enum):
    config = "config"
    loop = "loop"
    server = "server"
    product_repo = "product_repo"
    product_svc = "product_svc"
    mongodb_driver = "mongodb_driver"
    discounts_api = "discounts_api"


def configure(binder):
    inject.configure_once(binder, False)


def instance(key: Dependencies):
    return inject.instance(key)


async def dispose():
    inject.clear()
