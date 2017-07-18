.. raw:: html

   <div class="navheader">

12.1.25. sql\_column\_buffers
`Prev <conf-sql-attr-json.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-field-string.html>`__

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

.. rubric:: 12.1.25. sql\_column\_buffers
   :name: sql_column_buffers
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Per-column buffer sizes. Optional, default is empty (deduce the sizes
automatically). Applies to ``odbc``, ``mssql`` source types only.
Introduced in version 2.0.1-beta.

ODBC and MS SQL drivers sometimes can not return the maximum actual
column size to be expected. For instance, NVARCHAR(MAX) columns always
report their length as 2147483647 bytes to ``indexer`` even though the
actually used length is likely considerably less. However, the receiving
buffers still need to be allocated upfront, and their sizes have to be
determined. When the driver does not report the column length at all,
Sphinx allocates default 1 KB buffers for each non-char column, and 1 MB
buffers for each char column. Driver-reported column length also gets
clamped by an upper limit of 8 MB, so in case the driver reports
(almost) a 2 GB column length, it will be clamped and a 8 MB buffer will
be allocated instead for that column. These hard-coded limits can be
overridden using the ``sql_column_buffers`` directive, either in order
to save memory on actually shorter columns, or overcome the 8 MB limit
on actually longer columns. The directive values must be a
comma-separated lists of selected column names and sizes:

.. code:: programlisting

    sql_column_buffers = <colname>=<size>[K|M] [, ...]

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_query = SELECT id, mytitle, mycontent FROM documents
    sql_column_buffers = mytitle=64K, mycontent=10M

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+----------------------------------+------------------------------------------+
| `Prev <conf-sql-attr-json.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-sql-field-string.html>`__   |
+---------------------------------------+----------------------------------+------------------------------------------+
| 12.1.24. sql\_attr\_json              | `Home <index.html>`__            |  12.1.26. sql\_field\_string             |
+---------------------------------------+----------------------------------+------------------------------------------+

.. raw:: html

   </div>
