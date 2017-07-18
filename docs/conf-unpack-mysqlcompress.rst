.. raw:: html

   <div class="navheader">

12.1.46. unpack\_mysqlcompress
`Prev <conf-unpack-zlib.html>`__ 
12.1. Data source configuration options
 `Next <conf-unpack-mysqlcompress-maxsize.html>`__

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

.. rubric:: 12.1.46. unpack\_mysqlcompress
   :name: unpack_mysqlcompress
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Columns to unpack using MySQL UNCOMPRESS() algorithm. Multi-value,
optional, default value is empty list of columns. Applies to SQL source
types (``mysql``, ``pgsql``, ``mssql``) only. Introduced in version
0.9.9-rc1.

Columns specified using this directive will be unpacked by ``indexer``
using modified zlib algorithm used by MySQL COMPRESS() and UNCOMPRESS()
functions. When indexing on a different box than the database, this lets
you offload the database, and save on network traffic. The feature is
only available if zlib and zlib-devel were both available during build
time.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    unpack_mysqlcompress = body_compressed
    unpack_mysqlcompress = description_compressed

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------+----------------------------------+------------------------------------------------------+
| `Prev <conf-unpack-zlib.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-unpack-mysqlcompress-maxsize.html>`__   |
+-------------------------------------+----------------------------------+------------------------------------------------------+
| 12.1.45. unpack\_zlib               | `Home <index.html>`__            |  12.1.47. unpack\_mysqlcompress\_maxsize             |
+-------------------------------------+----------------------------------+------------------------------------------------------+

.. raw:: html

   </div>
