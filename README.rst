============================
collective.behavior.discount
============================

collective.behavior.discount provides discount related behavior in addition to price behavior to dexterity content types.

For farther documentation about price behavior, refer to the `collective.behavior.price
<http://pypi.python.org/pypi/collective.behavior.price>`_.

Currently tested with
---------------------

* Plone-4.3.6 with Python-2.7.x [taito]

Behavior
--------

The behavior can be added through the web or directly through the file system to the dexterity content type xml file like::

    <property name="behaviors">
      ...
      <element value="collective.behavior.discount.interfaces.IDiscount" />
      ...
    </property>
