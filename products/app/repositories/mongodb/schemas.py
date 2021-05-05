import bson
from marshmallow import Schema, fields, validate, EXCLUDE, post_dump

PAGE_LIMIT_DEFAULT = 10
PAGE_LIMIT_MAX = 100


class MongoDBId(fields.Raw):
    default_error_messages = {
        "invalid": "Not a valid id. It must be a 12-byte input or a 24-character hex string"
    }

    def _deserialize(self, value: str, attr, data, **kwargs):
        return str(value)

    def _serialize(self, value: bson.ObjectId, *args, **kwargs):
        try:
            value = bson.ObjectId(value)
        except InvalidId:
            raise self.make_error("invalid")
        return super()._serialize(value, *args, **kwargs)


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
    id = MongoDBId(data_key="_id")
    price_in_cents = fields.Integer(data_key="priceInCents")
    title = fields.String()
    description = fields.String()


class UserSchema(BaseSchema):
    id = MongoDBId(data_key="_id")
    first_name = fields.String(data_key="firstName")
    last_name = fields.String(data_key="lastName")
    date_of_birth = fields.Raw(data_key="dateOfBirth")


class PagingSchema(BaseSchema):
    limit = fields.Integer(validate=validate.Range(1, PAGE_LIMIT_MAX),
                           missing=PAGE_LIMIT_DEFAULT)
    offset = fields.Integer(missing=0)


PRODUCT_SCHEMA = ProductSchema(validate_dump=True)
USER_SCHEMA = UserSchema(validate_dump=True)
PAGING_SCHEMA = PagingSchema(validate_dump=True)
