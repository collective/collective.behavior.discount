import unittest


class TestIDiscount(unittest.TestCase):

    def test_subclass(self):
        from collective.behavior.discount.interfaces import IDiscount
        from collective.behavior.price.interfaces import IPrice
        self.assertTrue(issubclass(IDiscount, IPrice))

    def get_schema(self, name):
        """Get schema by name.

        :param name: Name of schema.
        :type name: str
        """
        from collective.behavior.discount.interfaces import IDiscount
        return IDiscount.get(name)

    def test_discount_enabled__instance(self):
        schema = self.get_schema('discount_enabled')
        from zope.schema import Bool
        self.assertIsInstance(schema, Bool)

    def test_discount_enabled__title(self):
        schema = self.get_schema('discount_enabled')
        self.assertEqual(schema.title, u'Discount Enabled')

    def test_discount_enabled__default(self):
        schema = self.get_schema('discount_enabled')
        self.assertFalse(schema.default)

    def test_price__instance(self):
        schema = self.get_schema('price')
        from zope.schema import Decimal
        self.assertIsInstance(schema, Decimal)

    def test_price__title(self):
        schema = self.get_schema('price')
        self.assertEqual(schema.title, u'Price including VAT')

    def test_price__required(self):
        schema = self.get_schema('price')
        self.assertTrue(schema.required)

    def test_discount_price__instance(self):
        schema = self.get_schema('discount_price')
        from zope.schema import Decimal
        self.assertIsInstance(schema, Decimal)

    def test_discount_price__title(self):
        schema = self.get_schema('discount_price')
        self.assertEqual(schema.title, u'Discount Price including VAT')

    def test_discount_price__required(self):
        schema = self.get_schema('discount_price')
        self.assertFalse(schema.required)

    def test_discount_start__instance(self):
        schema = self.get_schema('discount_start')
        from zope.schema import Date
        self.assertIsInstance(schema, Date)

    def test_discount_start__title(self):
        schema = self.get_schema('discount_start')
        self.assertEqual(schema.title, u'Discount Start Date')

    def test_discount_start__description(self):
        schema = self.get_schema('discount_start')
        self.assertFalse(schema.required)

    def test_discount_end__instance(self):
        schema = self.get_schema('discount_end')
        from zope.schema import Date
        self.assertIsInstance(schema, Date)

    def test_discount_end__title(self):
        schema = self.get_schema('discount_end')
        self.assertEqual(schema.title, u'Discount End Date')

    def test_discount_end__description(self):
        schema = self.get_schema('discount_end')
        self.assertFalse(schema.required)
