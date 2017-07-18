.. raw:: html

   <div class="navheader">

8.21. DROP FUNCTION syntax
`Prev <sphinxql-create-function.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-show-variables.html>`__

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

.. rubric:: 8.21. DROP FUNCTION syntax
   :name: drop-function-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    DROP FUNCTION udf_name

DROP FUNCTION statement, introduced in version 2.0.1-beta, deinstalls a
`user-defined function (UDF) <sphinx-udfs.html>`__ with the given name.
On success, the function is no longer available for use in subsequent
queries. Pending concurrent queries will not be affected and the library
unload, if necessary, will be postponed until those queries complete.
Example:

.. code:: programlisting

    mysql> DROP FUNCTION avgmva;
    Query OK, 0 rows affected (0.00 sec)

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------------+------------------------------------+--------------------------------------------+
| `Prev <sphinxql-create-function.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-show-variables.html>`__   |
+---------------------------------------------+------------------------------------+--------------------------------------------+
| 8.20. CREATE FUNCTION syntax                | `Home <index.html>`__              |  8.22. SHOW VARIABLES syntax               |
+---------------------------------------------+------------------------------------+--------------------------------------------+

.. raw:: html

   </div>
