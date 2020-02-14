# coding:utf-8

from marshmallow import Schema, fields


class InfoSchema(Schema):
    id = fields.Int(required=True)

    class Meta:
        strict = True
