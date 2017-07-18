.. raw:: html

   <div class="navheader">

8.18. SHOW TABLES syntax
`Prev <sphinxql-call-suggest.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-describe.html>`__

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

.. rubric:: 8.18. SHOW TABLES syntax
   :name: show-tables-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    SHOW TABLES [ LIKE pattern ]

SHOW TABLES statement, introduced in version 2.0.1-beta, enumerates all
currently active indexes along with their types. As of 2.0.1-beta,
existing index types are ``local``, ``distributed``, and ``rt``
respectively. Example:

.. code:: programlisting

    mysql> SHOW TABLES;
    +-------+-------------+
    | Index | Type        |
    +-------+-------------+
    | dist1 | distributed |
    | rt    | rt          |
    | test1 | local       |
    | test2 | local       |
    +-------+-------------+
    4 rows in set (0.00 sec)

Starting from version 2.1.1-beta, an optional LIKE clause is supported.
Refer to `Section 8.3, “SHOW META syntax” <sphinxql-show-meta.html>`__
for its syntax details.

.. code:: programlisting

    mysql> SHOW TABLES LIKE '%4';
    +-------+-------------+
    | Index | Type        |
    +-------+-------------+
    | dist4 | distributed |
    +-------+-------------+
    1 row in set (0.00 sec)

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+------------------------------------+--------------------------------------+
| `Prev <sphinxql-call-suggest.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-describe.html>`__   |
+------------------------------------------+------------------------------------+--------------------------------------+
| 8.17. CALL SUGGEST syntax                | `Home <index.html>`__              |  8.19. DESCRIBE syntax               |
+------------------------------------------+------------------------------------+--------------------------------------+

.. raw:: html

   </div>
