.. raw:: html

   <div class="navheader">

12.1.15. sql\_range\_step
`Prev <conf-sql-query-range.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-query-killlist.html>`__

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

.. rubric:: 12.1.15. sql\_range\_step
   :name: sql_range_step
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Range query step. Optional, default is 1024. Applies to SQL source types
(``mysql``, ``pgsql``, ``mssql``) only.

Only used when `ranged queries <sql.html#ranged-queries>`__ are enabled.
The full document IDs interval fetched by
`sql\_query\_range <conf-sql-query-range.html>`__ will be walked in this
big steps. For example, if min and max IDs fetched are 12 and 3456
respectively, and the step is 1000, indexer will call
`sql\_query <conf-sql-query.html>`__ several times with the following
substitutions:

.. raw:: html

   <div class="itemizedlist">

-  $start=12, $end=1011

-  $start=1012, $end=2011

-  $start=2012, $end=3011

-  $start=3012, $end=3456

.. raw:: html

   </div>

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_range_step = 1000

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+----------------------------------+--------------------------------------------+
| `Prev <conf-sql-query-range.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-sql-query-killlist.html>`__   |
+-----------------------------------------+----------------------------------+--------------------------------------------+
| 12.1.14. sql\_query\_range              | `Home <index.html>`__            |  12.1.16. sql\_query\_killlist             |
+-----------------------------------------+----------------------------------+--------------------------------------------+

.. raw:: html

   </div>
