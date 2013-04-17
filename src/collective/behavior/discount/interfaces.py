from collective.behavior.discount.schema import DiscountSchema
from collective.behavior.price.interfaces import IPrice


class IDiscount(DiscountSchema, IPrice):
    """Interface for behavior: Discount"""
