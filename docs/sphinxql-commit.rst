.. raw:: html

   <div class="navheader">

8.11. BEGIN, COMMIT, and ROLLBACK syntax
`Prev <sphinxql-set-transaction.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-begin.html>`__

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

.. rubric:: 8.11. BEGIN, COMMIT, and ROLLBACK syntax
   :name: begin-commit-and-rollback-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    START TRANSACTION | BEGIN
    COMMIT
    ROLLBACK
    SET AUTOCOMMIT = {0 | 1}

BEGIN, COMMIT, and ROLLBACK statements were introduced in version
1.10-beta. BEGIN statement (or its START TRANSACTION alias) forcibly
commits pending transaction, if any, and begins a new one. COMMIT
statement commits the current transaction, making all its changes
permanent. ROLLBACK statement rolls back the current transaction,
canceling all its changes. SET AUTOCOMMIT controls the autocommit mode
in the active session.

AUTOCOMMIT is set to 1 by default, meaning that every statement that
performs any changes on any index is implicitly wrapped in BEGIN and
COMMIT.

Transactions are limited to a single RT index, and also limited in size.
They are atomic, consistent, overly isolated, and durable. Overly
isolated means that the changes are not only invisible to the concurrent
transactions but even to the current session itself.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------------+------------------------------------+-----------------------------------+
| `Prev <sphinxql-set-transaction.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-begin.html>`__   |
+---------------------------------------------+------------------------------------+-----------------------------------+
| 8.10. SET TRANSACTION syntax                | `Home <index.html>`__              |  8.12. BEGIN syntax               |
+---------------------------------------------+------------------------------------+-----------------------------------+

.. raw:: html

   </div>
