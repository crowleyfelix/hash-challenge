# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: discounts.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='discounts.proto',
  package='discounts',
  syntax='proto3',
  serialized_options=b'Z\017discounts/proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x64iscounts.proto\x12\tdiscounts\x1a\x1fgoogle/protobuf/timestamp.proto\"7\n\x10\x43\x61lculateRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\"W\n\x11\x43\x61lculateResponse\x12\x1d\n\x04user\x18\x01 \x01(\x0b\x32\x0f.discounts.User\x12#\n\x07product\x18\x02 \x01(\x0b\x32\x12.discounts.Product\"l\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x31\n\rdate_of_birth\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"x\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\t\x12\x16\n\x0eprice_in_cents\x18\x02 \x01(\x03\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12%\n\x08\x64iscount\x18\x05 \x01(\x0b\x32\x13.discounts.Discount\"6\n\x08\x44iscount\x12\x12\n\npercentage\x18\x01 \x01(\x02\x12\x16\n\x0evalue_in_cents\x18\x02 \x01(\x03\x32^\n\x12\x44iscountCalculator\x12H\n\tCalculate\x12\x1b.discounts.CalculateRequest\x1a\x1c.discounts.CalculateResponse\"\x00\x42\x11Z\x0f\x64iscounts/protob\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_CALCULATEREQUEST = _descriptor.Descriptor(
  name='CalculateRequest',
  full_name='discounts.CalculateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_id', full_name='discounts.CalculateRequest.product_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='discounts.CalculateRequest.user_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=118,
)


_CALCULATERESPONSE = _descriptor.Descriptor(
  name='CalculateResponse',
  full_name='discounts.CalculateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='discounts.CalculateResponse.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product', full_name='discounts.CalculateResponse.product', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=207,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='discounts.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='discounts.User.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='discounts.User.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='discounts.User.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date_of_birth', full_name='discounts.User.date_of_birth', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=317,
)


_PRODUCT = _descriptor.Descriptor(
  name='Product',
  full_name='discounts.Product',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='discounts.Product.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price_in_cents', full_name='discounts.Product.price_in_cents', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='discounts.Product.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='discounts.Product.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='discount', full_name='discounts.Product.discount', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=319,
  serialized_end=439,
)


_DISCOUNT = _descriptor.Descriptor(
  name='Discount',
  full_name='discounts.Discount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='percentage', full_name='discounts.Discount.percentage', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value_in_cents', full_name='discounts.Discount.value_in_cents', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=441,
  serialized_end=495,
)

_CALCULATERESPONSE.fields_by_name['user'].message_type = _USER
_CALCULATERESPONSE.fields_by_name['product'].message_type = _PRODUCT
_USER.fields_by_name['date_of_birth'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PRODUCT.fields_by_name['discount'].message_type = _DISCOUNT
DESCRIPTOR.message_types_by_name['CalculateRequest'] = _CALCULATEREQUEST
DESCRIPTOR.message_types_by_name['CalculateResponse'] = _CALCULATERESPONSE
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Product'] = _PRODUCT
DESCRIPTOR.message_types_by_name['Discount'] = _DISCOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CalculateRequest = _reflection.GeneratedProtocolMessageType('CalculateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CALCULATEREQUEST,
  '__module__' : 'discounts_pb2'
  # @@protoc_insertion_point(class_scope:discounts.CalculateRequest)
  })
_sym_db.RegisterMessage(CalculateRequest)

CalculateResponse = _reflection.GeneratedProtocolMessageType('CalculateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CALCULATERESPONSE,
  '__module__' : 'discounts_pb2'
  # @@protoc_insertion_point(class_scope:discounts.CalculateResponse)
  })
_sym_db.RegisterMessage(CalculateResponse)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'discounts_pb2'
  # @@protoc_insertion_point(class_scope:discounts.User)
  })
_sym_db.RegisterMessage(User)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCT,
  '__module__' : 'discounts_pb2'
  # @@protoc_insertion_point(class_scope:discounts.Product)
  })
_sym_db.RegisterMessage(Product)

Discount = _reflection.GeneratedProtocolMessageType('Discount', (_message.Message,), {
  'DESCRIPTOR' : _DISCOUNT,
  '__module__' : 'discounts_pb2'
  # @@protoc_insertion_point(class_scope:discounts.Discount)
  })
_sym_db.RegisterMessage(Discount)


DESCRIPTOR._options = None

_DISCOUNTCALCULATOR = _descriptor.ServiceDescriptor(
  name='DiscountCalculator',
  full_name='discounts.DiscountCalculator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=497,
  serialized_end=591,
  methods=[
  _descriptor.MethodDescriptor(
    name='Calculate',
    full_name='discounts.DiscountCalculator.Calculate',
    index=0,
    containing_service=None,
    input_type=_CALCULATEREQUEST,
    output_type=_CALCULATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DISCOUNTCALCULATOR)

DESCRIPTOR.services_by_name['DiscountCalculator'] = _DISCOUNTCALCULATOR

# @@protoc_insertion_point(module_scope)