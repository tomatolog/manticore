.. raw:: html

   <div class="navheader">

12.1.29. sql\_query\_post\_index
`Prev <conf-sql-query-post.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-ranged-throttle.html>`__

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

.. rubric:: 12.1.29. sql\_query\_post\_index
   :name: sql_query_post_index
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Post-index query. Optional, default value is empty. Applies to SQL
source types (``mysql``, ``pgsql``, ``mssql``) only.

This query is executed when indexing is fully and successfully
completed. If this query produces errors, they are reported as warnings,
but indexing is **not** terminated. It’s result set is ignored.
``$maxid`` macro can be used in its text; it will be expanded to maximum
document ID which was actually fetched from the database during
indexing. If no documents were indexed, $maxid will be expanded to 0.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_query_post_index = REPLACE INTO counters ( id, val ) \
        VALUES ( 'max_indexed_id', $maxid )

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------+----------------------------------+---------------------------------------------+
| `Prev <conf-sql-query-post.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-sql-ranged-throttle.html>`__   |
+----------------------------------------+----------------------------------+---------------------------------------------+
| 12.1.28. sql\_query\_post              | `Home <index.html>`__            |  12.1.30. sql\_ranged\_throttle             |
+----------------------------------------+----------------------------------+---------------------------------------------+

.. raw:: html

   </div>
