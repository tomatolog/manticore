.. raw:: html

   <div class="navheader">

12.1.28. sql\_query\_post
`Prev <conf-sql-file-field.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-query-post-index.html>`__

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

.. rubric:: 12.1.28. sql\_query\_post
   :name: sql_query_post
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Post-fetch query. Optional, default value is empty. Applies to SQL
source types (``mysql``, ``pgsql``, ``mssql``) only.

This query is executed immediately after
`sql\_query <conf-sql-query.html>`__ completes successfully. When
post-fetch query produces errors, they are reported as warnings, but
indexing is **not** terminated. It’s result set is ignored. Note that
indexing is **not** yet completed at the point when this query gets
executed, and further indexing still may fail. Therefore, any permanent
updates should not be done from here. For instance, updates on helper
table that permanently change the last successfully indexed ID should
not be run from post-fetch query; they should be run from `post-index
query <conf-sql-query-post-index.html>`__ instead.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_query_post = DROP TABLE my_tmp_table

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------+----------------------------------+----------------------------------------------+
| `Prev <conf-sql-file-field.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-sql-query-post-index.html>`__   |
+----------------------------------------+----------------------------------+----------------------------------------------+
| 12.1.27. sql\_file\_field              | `Home <index.html>`__            |  12.1.29. sql\_query\_post\_index            |
+----------------------------------------+----------------------------------+----------------------------------------------+

.. raw:: html

   </div>
