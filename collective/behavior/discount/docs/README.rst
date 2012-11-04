============================
collective.behavior.discount
============================

collective.behavior.discount provides discount related behavior in addition to price behavior to dexterity content types.

For farther documentation about price behavior, refer to the `collective.behavior.price
<http://pypi.python.org/pypi/collective.behavior.price>`_.

Currently tested with
---------------------

* Plone-4.2.2 [taito]

Behavior
--------

The behavior can be added through the web or directly through the file system to the dexterity content type xml file like::

    <property name="behaviors">
      ...
      <element value="collective.behavior.discount.interfaces.IDiscount" />
      ...
    </property>

Farther Documentation URL
-------------------------

`http://packages.python.org/collective.behavior.discount/
<http://packages.python.org/collective.behavior.discount/>`_

Repository URL
--------------

`https://github.com/collective/collective.behavior.discount/
<https://github.com/collective/collective.behavior.discount/>`_
