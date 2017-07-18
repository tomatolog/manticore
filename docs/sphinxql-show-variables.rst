.. raw:: html

   <div class="navheader">

8.22. SHOW VARIABLES syntax
`Prev <sphinxql-drop-function.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-show-collation.html>`__

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

.. rubric:: 8.22. SHOW VARIABLES syntax
   :name: show-variables-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    SHOW [{GLOBAL | SESSION}] VARIABLES [WHERE variable_name='xxx']

**SHOW VARIABLES** statement was added in version 2.0.1-beta to improve
compatibility with 3rd party MySQL connectors and frameworks that
automatically execute this statement. The WHERE option was added in
version 2.1.1-beta.

In version 2.0.1-beta, it did nothing.

Starting from version 2.0.2-beta, it returns the current values of a few
server-wide variables. Also, support for GLOBAL and SESSION clauses was
added.

.. code:: programlisting

    mysql> SHOW GLOBAL VARIABLES;
    +----------------------+----------+
    | Variable_name        | Value    |
    +----------------------+----------+
    | autocommit           | 1        |
    | collation_connection | libc_ci  |
    | query_log_format     | sphinxql |
    | log_level            | info     |
    +----------------------+----------+
    4 rows in set (0.00 sec)

Starting from 2.1.1-beta, support for WHERE variable\_name clause was
added, to help certain connectors.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+------------------------------------+--------------------------------------------+
| `Prev <sphinxql-drop-function.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-show-collation.html>`__   |
+-------------------------------------------+------------------------------------+--------------------------------------------+
| 8.21. DROP FUNCTION syntax                | `Home <index.html>`__              |  8.23. SHOW COLLATION syntax               |
+-------------------------------------------+------------------------------------+--------------------------------------------+

.. raw:: html

   </div>
