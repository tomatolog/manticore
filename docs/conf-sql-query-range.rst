.. raw:: html

   <div class="navheader">

12.1.14. sql\_query\_range
`Prev <conf-sql-joined-field.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-range-step.html>`__

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

.. rubric:: 12.1.14. sql\_query\_range
   :name: sql_query_range
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Range query setup. Optional, default is empty. Applies to SQL source
types (``mysql``, ``pgsql``, ``mssql``) only.

Setting this option enables ranged document fetch queries (see `the
section called “Ranged queries” <sql.html#ranged-queries>`__). Ranged
queries are useful to avoid notorious MyISAM table locks when indexing
lots of data. (They also help with other less notorious issues, such as
reduced performance caused by big result sets, or additional resources
consumed by InnoDB to serialize big read transactions.)

The query specified in this option must fetch min and max document IDs
that will be used as range boundaries. It must return exactly two
integer fields, min ID first and max ID second; the field names are
ignored.

When ranged queries are enabled, `sql\_query <conf-sql-query.html>`__
will be required to contain ``$start`` and ``$end`` macros (because it
obviously would be a mistake to index the whole table many times over).
Note that the intervals specified by ``$start``..\ ``$end`` will not
overlap, so you should **not** remove document IDs that are exactly
equal to ``$start`` or ``$end`` from your query. The example in `the
section called “Ranged queries” <sql.html#ranged-queries>`__)
illustrates that; note how it uses greater-or-equal and less-or-equal
comparisons.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_query_range = SELECT MIN(id),MAX(id) FROM documents

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+----------------------------------+----------------------------------------+
| `Prev <conf-sql-joined-field.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-sql-range-step.html>`__   |
+------------------------------------------+----------------------------------+----------------------------------------+
| 12.1.13. sql\_joined\_field              | `Home <index.html>`__            |  12.1.15. sql\_range\_step             |
+------------------------------------------+----------------------------------+----------------------------------------+

.. raw:: html

   </div>
