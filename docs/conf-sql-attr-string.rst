.. raw:: html

   <div class="navheader">

12.1.23. sql\_attr\_string
`Prev <conf-sql-attr-multi.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-attr-json.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect2">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 12.1.23. sql\_attr\_string
   :name: sql_attr_string
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

String attribute declaration. Multi-value (ie. there may be more than
one such attribute declared), optional. Applies to SQL source types
(``mysql``, ``pgsql``, ``mssql``) only. Introduced in version 1.10-beta.

String attributes can store arbitrary strings attached to every
document. There’s a fixed size limit of 4 MB per value. Also,
``searchd`` will currently cache all the values in RAM, which is an
additional implicit limit.

Starting from 2.0.1-beta string attributes can be used for sorting and
grouping(ORDER BY, GROUP BY, WITHIN GROUP ORDER BY). Note that
attributes declared using ``sql_attr_string`` will **not** be full-text
indexed; you can use `sql\_field\_string <conf-sql-field-string.html>`__
directive for that.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_attr_string = title # will be stored but will not be indexed

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------+----------------------------------+---------------------------------------+
| `Prev <conf-sql-attr-multi.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-sql-attr-json.html>`__   |
+----------------------------------------+----------------------------------+---------------------------------------+
| 12.1.22. sql\_attr\_multi              | `Home <index.html>`__            |  12.1.24. sql\_attr\_json             |
+----------------------------------------+----------------------------------+---------------------------------------+

.. raw:: html

   </div>
