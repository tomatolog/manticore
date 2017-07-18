.. raw:: html

   <div class="navheader">

12.1.30. sql\_ranged\_throttle
`Prev <conf-sql-query-post-index.html>`__ 
12.1. Data source configuration options
 `Next <conf-xmlpipe-command.html>`__

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

.. rubric:: 12.1.30. sql\_ranged\_throttle
   :name: sql_ranged_throttle
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Ranged query throttling period, in milliseconds. Optional, default is 0
(no throttling). Applies to SQL source types (``mysql``, ``pgsql``,
``mssql``) only.

Throttling can be useful when indexer imposes too much load on the
database server. It causes the indexer to sleep for given amount of
milliseconds once per each ranged query step. This sleep is
unconditional, and is performed before the fetch query.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_ranged_throttle = 1000 # sleep for 1 sec before each query step

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------------+----------------------------------+-----------------------------------------+
| `Prev <conf-sql-query-post-index.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-xmlpipe-command.html>`__   |
+----------------------------------------------+----------------------------------+-----------------------------------------+
| 12.1.29. sql\_query\_post\_index             | `Home <index.html>`__            |  12.1.31. xmlpipe\_command              |
+----------------------------------------------+----------------------------------+-----------------------------------------+

.. raw:: html

   </div>
