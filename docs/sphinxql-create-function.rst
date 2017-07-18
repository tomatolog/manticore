.. raw:: html

   <div class="navheader">

8.20. CREATE FUNCTION syntax
`Prev <sphinxql-describe.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-drop-function.html>`__

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

.. rubric:: 8.20. CREATE FUNCTION syntax
   :name: create-function-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    CREATE FUNCTION udf_name
        RETURNS {INT | INTEGER | BIGINT | FLOAT | STRING}
        SONAME 'udf_lib_file'

CREATE FUNCTION statement, introduced in version 2.0.1-beta, installs a
`user-defined function (UDF) <sphinx-udfs.html>`__ with the given name
and type from the given library file. The library file must reside in a
trusted `plugin\_dir <conf-plugin-dir.html>`__ directory. On success,
the function is available for use in all subsequent queries that the
server receives. Example:

.. code:: programlisting

    mysql> CREATE FUNCTION avgmva RETURNS INTEGER SONAME 'udfexample.dll';
    Query OK, 0 rows affected (0.03 sec)

    mysql> SELECT *, AVGMVA(tag) AS q from test1;
    +------+--------+---------+-----------+
    | id   | weight | tag     | q         |
    +------+--------+---------+-----------+
    |    1 |      1 | 1,3,5,7 | 4.000000  |
    |    2 |      1 | 2,4,6   | 4.000000  |
    |    3 |      1 | 15      | 15.000000 |
    |    4 |      1 | 7,40    | 23.500000 |
    +------+--------+---------+-----------+

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------+------------------------------------+-------------------------------------------+
| `Prev <sphinxql-describe.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-drop-function.html>`__   |
+--------------------------------------+------------------------------------+-------------------------------------------+
| 8.19. DESCRIBE syntax                | `Home <index.html>`__              |  8.21. DROP FUNCTION syntax               |
+--------------------------------------+------------------------------------+-------------------------------------------+

.. raw:: html

   </div>
