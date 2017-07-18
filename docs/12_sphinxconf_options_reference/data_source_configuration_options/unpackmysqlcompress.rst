unpack\_mysqlcompress
~~~~~~~~~~~~~~~~~~~~~

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

Example:
^^^^^^^^

::


    unpack_mysqlcompress = body_compressed
    unpack_mysqlcompress = description_compressed

