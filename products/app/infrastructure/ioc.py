import inject


class Dependencies:
    product_repo = "product_repo"
    product_svc = "product_svc"
    mongo_driver = "mongo_driver"


def configure(binder):
    inject.configure(binder, False)


def instance(key: Dependencies):
    return inject.instance(key)
