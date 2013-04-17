from collective.behavior.discount import _
from collective.behavior.price.schema import PriceSchema
from zope import schema


class DiscountSchema(PriceSchema):
    """Schema for behavior: Discount"""

    price = schema.Decimal(
        title=_(u"Price including VAT"),
        required=True)

    discount_enabled = schema.Bool(
        title=_(u"Discount Enabled"),
        required=False)

    discount_price = schema.Decimal(
        title=_(u'Discount Price including VAT'),
        required=False)

    discount_start = schema.Date(
        title=_(u'Discount Start Date'),
        description=_(u''),
        required=False)

    discount_end = schema.Date(
        title=_(u'Discount End Date'),
        description=_(u''),
        required=False)
