import mock
import unittest


class TestDiscount(unittest.TestCase):

    def test_subclass(self):
        from collective.behavior.discount.behavior import Discount
        self.assertTrue(issubclass(Discount, object))

    def create_instance(self, context=mock.Mock()):
        from collective.behavior.discount.behavior import Discount
        return Discount(context)

    def test_instance(self):
        instance = self.create_instance()
        from collective.behavior.discount.behavior import Discount
        self.assertIsInstance(instance, Discount)

    def test_instance_provides_IDiscount(self):
        instance = self.create_instance()
        from collective.behavior.discount.interfaces import IDiscount
        self.assertTrue(IDiscount.providedBy(instance))

    @mock.patch('collective.behavior.price.behavior.getUtility')
    def test_instance__verifyObject(self, getUtility):
        instance = self.create_instance()
        from collective.behavior.discount.interfaces import IDiscount
        from zope.interface.verify import verifyObject
        self.assertTrue(verifyObject(IDiscount, instance))

    def test_instance__discount_enabled(self):
        """First time access to discount_enabled"""
        context = object()
        instance = self.create_instance(context=context)
        self.assertFalse(instance.discount_enabled)

    def test_instance__discount_enabled__set_False(self):
        context = mock.Mock()
        instance = self.create_instance(context=context)
        instance.discount_enabled = False
        self.assertFalse(instance.discount_enabled)
        self.assertFalse(instance.context.discount_enabled)

    def test_instance__discount_enabled__set_True(self):
        context = mock.Mock()
        instance = self.create_instance(context=context)
        instance.discount_enabled = True
        self.assertTrue(instance.discount_enabled)
        self.assertTrue(instance.context.discount_enabled)

    def set_discount_enabled(self, value):
        context = mock.Mock()
        instance = self.create_instance(context=context)
        instance.discount_enabled = value

    def test_instance__discount_enabled__ValueError(self):
        self.assertRaises(ValueError, lambda: self.set_discount_enabled('AAA'))

    def test_instance__price_empty(self):
        """First time access to discount_price"""
        context = object()
        instance = self.create_instance(context=context)
        self.assertIsNone(instance.discount_price)

    def test_instance__discount_price_not_empty(self):
        """Price is not empty"""
        context = mock.Mock()
        from decimal import Decimal
        discount_price = Decimal('5.00')
        context.discount_price = discount_price
        instance = self.create_instance(context=context)
        self.assertEqual(instance.discount_price, discount_price)

    def set_discount_price(self, instance, discount_price):
        """Setting discount_price to instance."""
        instance.discount_price = discount_price

    def test_instance__price__ValueError(self):
        """Raise ValueError when setting other than Decimal."""
        instance = self.create_instance()
        self.assertRaises(ValueError, lambda: self.set_discount_price(instance, 'AAA'))

    @mock.patch('collective.behavior.price.behavior.getUtility')
    def test_instance__price__price(self, getUtility):
        """"""
        getUtility().forInterface().default_currency = 'EUR'
        context = mock.Mock()
        instance = self.create_instance(context=context)
        from decimal import Decimal
        discount_price = Decimal('5.00')
        instance.discount_price = discount_price
        self.assertEqual(instance.context.discount_price, discount_price)
        from moneyed import Money
        discount_money = Money(discount_price, currency='EUR')
        self.assertEqual(instance.context.discount_money, discount_money)
        self.assertEqual(instance.discount_money, discount_money)

    def test_instance__money_empty(self):
        """First time access to discount_money"""
        context = object()
        instance = self.create_instance(context=context)
        self.assertIsNone(instance.discount_money)

    def set_money(self, instance, discount_money):
        """Setting discount_money to instance."""
        instance.discount_money = discount_money

    def test_instance__money__ValueError(self):
        """Raise ValueError when setting other than Money."""
        instance = self.create_instance()
        self.assertRaises(ValueError, lambda: self.set_money(instance, 'AAA'))

    def test_instance__money__set(self):
        instance = self.create_instance()
        from moneyed import Money
        from decimal import Decimal
        discount_money = Money(Decimal('5.00'), currency="EUR")
        instance.discount_money = discount_money
        self.assertEqual(instance.discount_money, discount_money)

    def test_instance___set_date(self):
        context = mock.Mock()
        instance = self.create_instance(context=context)
        from datetime import date
        day = date(2012, 07, 01)
        instance._set_date(day, 'DAY')
        self.assertEqual(instance.context.DAY, day)

    def test_instance___set_date__ValueError(self):
        context = mock.Mock()
        instance = self.create_instance(context=context)
        self.assertRaises(ValueError, lambda: instance._set_date('AAA', 'DAY'))

    def test_instance__discount_start(self):
        context = mock.Mock()
        instance = self.create_instance(context=context)
        instance._set_date = mock.Mock()
        instance.discount_start = 'AAA'
        instance._set_date.assert_called_with('AAA', 'discount_start')

    def test_instance__discount_end(self):
        context = mock.Mock()
        instance = self.create_instance(context=context)
        instance._set_date = mock.Mock()
        instance.discount_end = 'AAA'
        instance._set_date.assert_called_with('AAA', 'discount_end')
