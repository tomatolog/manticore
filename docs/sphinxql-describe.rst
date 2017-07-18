.. raw:: html

   <div class="navheader">

8.19. DESCRIBE syntax
`Prev <sphinxql-show-tables.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-create-function.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect1">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 8.19. DESCRIBE syntax
   :name: describe-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    {DESC | DESCRIBE} index [ LIKE pattern ]

DESCRIBE statement, introduced in version 2.0.1-beta, lists index
columns and their associated types. Columns are document ID, full-text
fields, and attributes. The order matches that in which fields and
attributes are expected by INSERT and REPLACE statements. As of
2.0.1-beta, column types are ``field``, ``integer``, ``timestamp``,
``ordinal``, ``bool``, ``float``, ``bigint``, ``string``, and ``mva``.
ID column will be typed either ``integer`` or ``bigint`` based on
whether the binaries were built with 32-bit or 64-bit document ID
support. Example:

.. code:: programlisting

    mysql> DESC rt;
    +---------+---------+
    | Field   | Type    |
    +---------+---------+
    | id      | integer |
    | title   | field   |
    | content | field   |
    | gid     | integer |
    +---------+---------+
    4 rows in set (0.00 sec)

Starting from version 2.1.1-beta, an optional LIKE clause is supported.
Refer to `Section 8.3, “SHOW META syntax” <sphinxql-show-meta.html>`__
for its syntax details.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+------------------------------------+---------------------------------------------+
| `Prev <sphinxql-show-tables.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-create-function.html>`__   |
+-----------------------------------------+------------------------------------+---------------------------------------------+
| 8.18. SHOW TABLES syntax                | `Home <index.html>`__              |  8.20. CREATE FUNCTION syntax               |
+-----------------------------------------+------------------------------------+---------------------------------------------+

.. raw:: html

   </div>
