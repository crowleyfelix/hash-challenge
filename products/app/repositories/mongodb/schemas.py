from marshmallow import Schema, fields, validate, EXCLUDE, post_dump

PAGE_LIMIT_DEFAULT = 10
PAGE_LIMIT_MAX = 100

class BaseSchema(Schema):
    class Meta:
        strict = True
        unknown = EXCLUDE

    def __init__(self, *args, validate_dump=False, **kwargs):
        self._validate_dump = validate_dump
        super().__init__(*args, **kwargs)

    @post_dump
    def _validate_on_dump(self, data, **_):
        """Valida o payload gerado contra o próprio Schema."""
        if self._validate_dump:
            self.validate(data)

        return data

class ProductSchema(BaseSchema):
    id = fields.String()
    price_in_cents = fields.Integer()
    title = fields.String()
    description = fields.String()

class PagingSchema(BaseSchema):
    limit = fields.Integer(validate=validate.Range(1, PAGE_LIMIT_MAX),
                        missing=PAGE_LIMIT_DEFAULT)
    offset = fields.Integer(missing=0)

PRODUCT_SCHEMA = ProductSchema(validate_dump=True)
PAGING_SCHEMA = PagingSchema(validate_dump=True)