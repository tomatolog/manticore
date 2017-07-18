.. raw:: html

   <div class="navheader">

12.1.45. unpack\_zlib
`Prev <conf-mssql-winauth.html>`__ 
12.1. Data source configuration options
 `Next <conf-unpack-mysqlcompress.html>`__

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

.. rubric:: 12.1.45. unpack\_zlib
   :name: unpack_zlib
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Columns to unpack using zlib (aka deflate, aka gunzip). Multi-value,
optional, default value is empty list of columns. Applies to SQL source
types (``mysql``, ``pgsql``, ``mssql``) only. Introduced in version
0.9.9-rc1.

Columns specified using this directive will be unpacked by ``indexer``
using standard zlib algorithm (called deflate and also implemented by
``gunzip``). When indexing on a different box than the database, this
lets you offload the database, and save on network traffic. The feature
is only available if zlib and zlib-devel were both available during
build time.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    unpack_zlib = col1
    unpack_zlib = col2

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+----------------------------------+----------------------------------------------+
| `Prev <conf-mssql-winauth.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-unpack-mysqlcompress.html>`__   |
+---------------------------------------+----------------------------------+----------------------------------------------+
| 12.1.44. mssql\_winauth               | `Home <index.html>`__            |  12.1.46. unpack\_mysqlcompress              |
+---------------------------------------+----------------------------------+----------------------------------------------+

.. raw:: html

   </div>
