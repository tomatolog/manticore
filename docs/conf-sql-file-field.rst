.. raw:: html

   <div class="navheader">

12.1.27. sql\_file\_field
`Prev <conf-sql-field-string.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-query-post.html>`__

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

.. rubric:: 12.1.27. sql\_file\_field
   :name: sql_file_field
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

File based field declaration. Applies to SQL source types (``mysql``,
``pgsql``, ``mssql``) only. Introduced in version 1.10-beta.

This directive makes ``indexer`` interpret field contents as a file
name, and load and index the referred file. Files larger than
`max\_file\_field\_buffer <conf-max-file-field-buffer.html>`__ in size
are skipped. Any errors during the file loading (IO errors, missed
limits, etc) will be reported as indexing warnings and will **not**
early terminate the indexing. No content will be indexed for such files.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_file_field = my_file_path # load and index files referred to by my_file_path

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+----------------------------------+----------------------------------------+
| `Prev <conf-sql-field-string.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-sql-query-post.html>`__   |
+------------------------------------------+----------------------------------+----------------------------------------+
| 12.1.26. sql\_field\_string              | `Home <index.html>`__            |  12.1.28. sql\_query\_post             |
+------------------------------------------+----------------------------------+----------------------------------------+

.. raw:: html

   </div>
