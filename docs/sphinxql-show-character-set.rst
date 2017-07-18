.. raw:: html

   <div class="navheader">

8.24. SHOW CHARACTER SET syntax
`Prev <sphinxql-show-collation.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-update.html>`__

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

.. rubric:: 8.24. SHOW CHARACTER SET syntax
   :name: show-character-set-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    SHOW CHARACTER SET

Added in version 2.1.1-beta, this is currently a placeholder query that
does nothing and reports that a UTF-8 character set is available. It was
added in order to keep compatibility with frameworks and connectors that
automatically execute this statement.

.. code:: programlisting

    mysql> SHOW CHARACTER SET;
    +---------+---------------+-------------------+--------+
    | Charset | Description   | Default collation | Maxlen |
    +---------+---------------+-------------------+--------+
    | utf8    | UTF-8 Unicode | utf8_general_ci   | 3      |
    +---------+---------------+-------------------+--------+
    1 row in set (0.00 sec)

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+------------------------------------+------------------------------------+
| `Prev <sphinxql-show-collation.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-update.html>`__   |
+--------------------------------------------+------------------------------------+------------------------------------+
| 8.23. SHOW COLLATION syntax                | `Home <index.html>`__              |  8.25. UPDATE syntax               |
+--------------------------------------------+------------------------------------+------------------------------------+

.. raw:: html

   </div>
