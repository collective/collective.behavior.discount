from collective.behavior.discount.interfaces import IDiscount
from collective.behavior.price.behavior import Price
from datetime import date
from plone.directives import form
from rwproperty import getproperty
from rwproperty import setproperty
from zope.interface import alsoProvides
from zope.interface import implements

import logging

logger = logging.getLogger(__name__)


alsoProvides(IDiscount, form.IFormFieldProvider)


class Discount(Price):
    """
    """
    implements(IDiscount)

    @getproperty
    def discount_enabled(self):
        return getattr(self.context, 'discount_enabled', False)

    @setproperty
    def discount_enabled(self, value):
        """Set discount_enabled as Boolean

        :param value: True or False
        :type value: bool
        """
        if value is not True:
            if value is not False:
                raise ValueError('Not Bool')
        setattr(self.context, 'discount_enabled', value)

    @getproperty
    def discount_price(self):
        return getattr(self.context, 'discount_price', None)

    @setproperty
    def discount_price(self, value):
        """Setting discount_price as Decimal and discount_money as Money.

        :param value: Price value such as 5.00, 5,00 nor 1800.
        :type value: decimal.Decimal
        """
        self._set_price(value, name='discount_')

    @getproperty
    def discount_money(self):
        return getattr(self.context, 'discount_money', None)

    @setproperty
    def discount_money(self, value):
        """Setting discount_money as Money.

        :param value: Money instance.
        :type value: moneyed.Money
        """
        self._set_money(value, name='discount_')

    @getproperty
    def discount_start(self):
        return getattr(self.context, 'discount_start', None)

    def _set_date(self, value, name):
        """Setting discount_start as datetime.date.

        :param value: Starting date for discount.
        :type value: datetime.date

        :param name: Name of field.
        :type name: str
        """
        if isinstance(value, date):
            setattr(self.context, name, value)
        else:
            raise ValueError('Not datetime.date.')

    @setproperty
    def discount_start(self, value):
        """Setting discount_start as datetime.date.

        :param value: Starting date for discount.
        :type value: datetime.date
        """
        self._set_date(value, 'discount_start')

    @getproperty
    def discount_end(self):
        return getattr(self.context, 'discount_end', None)

    @setproperty
    def discount_end(self, value):
        """Setting discount_end as datetime.date.

        :param value: Starting date for discount.
        :type value: datetime.date
        """
        self._set_date(value, 'discount_end')
