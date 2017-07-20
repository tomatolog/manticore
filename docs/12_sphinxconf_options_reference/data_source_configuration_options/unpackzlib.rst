unpack\_zlib
~~~~~~~~~~~~

Columns to unpack using zlib (aka deflate, aka gunzip). Multi-value,
optional, default value is empty list of columns. Applies to SQL source
types (``mysql``, ``pgsql``, ``mssql``) only.

Columns specified using this directive will be unpacked by ``indexer``
using standard zlib algorithm (called deflate and also implemented by
``gunzip``). When indexing on a different box than the database, this
lets you offload the database, and save on network traffic. The feature
is only available if zlib and zlib-devel were both available during
build time.

Example:
^^^^^^^^

::


    unpack_zlib = col1
    unpack_zlib = col2

