from collective.behavior.discount import _
from collective.behavior.price.interfaces import IPrice
from zope.schema import Bool
from zope.schema import Date
from zope.schema import Decimal


class IDiscount(IPrice):
    """Interface for Discount behavior."""

    discount_enabled = Bool(
        title=_(u"Discount Enabled"),
        required=False)

    discount_price = Decimal(
        title=_(u'Discount Price'),
        required=False)

    discount_start = Date(
        title=_(u'Discount Start Date'),
        description=_(u''),
        required=False)

    discount_end = Date(
        title=_(u'Discount End Date'),
        description=_(u''),
        required=False)
