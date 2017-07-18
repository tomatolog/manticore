.. raw:: html

   <div class="navheader">

8.10. SET TRANSACTION syntax
`Prev <sphinxql-set.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-commit.html>`__

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

.. rubric:: 8.10. SET TRANSACTION syntax
   :name: set-transaction-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    SET TRANSACTION ISOLATION LEVEL { READ UNCOMMITTED
        | READ COMMITTED
        | REPEATABLE READ
        | SERIALIZABLE }

SET TRANSACTION statement, introduced in version 2.0.2-beta, does
nothing. It was implemented to maintain compatibility with 3rd party
MySQL client libraries, connectors, and frameworks that may need to run
this statement when connecting.

Example:

.. code:: programlisting

    mysql> SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
    Query OK, 0 rows affected (0.00 sec)

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------+------------------------------------+---------------------------------------------+
| `Prev <sphinxql-set.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-commit.html>`__            |
+---------------------------------+------------------------------------+---------------------------------------------+
| 8.9. SET syntax                 | `Home <index.html>`__              |  8.11. BEGIN, COMMIT, and ROLLBACK syntax   |
+---------------------------------+------------------------------------+---------------------------------------------+

.. raw:: html

   </div>
