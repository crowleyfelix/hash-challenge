from marshmallow import Schema, fields

PAGE_LIMIT_DEFAULT = 10
PAGE_LIMIT_MAX = 100

class BaseSchema(Schema):
    pass

class ProductSchema(Schema):
    id = fields.String()
    price_in_cents = fields.Integer()
    title = fields.String()
    description = fields.String()

class PagingSchema(Schema):
    limit = fields.Integer(validate=validate.Range(1, PAGE_LIMIT_MAX),
                        missing=PAGE_LIMIT_DEFAULT)
    offset = fields.Integer(missing=0)

PRODUCT_SCHEMA = ProductSchema( )
PAGING_SCHEMA = PagingSchema()