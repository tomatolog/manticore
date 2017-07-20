unpack\_mysqlcompress\_maxsize
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Buffer size for UNCOMPRESS()ed data. Optional, default value is 16M.

When using
`unpack\_mysqlcompress <../../data_source_configuration_options/unpackmysqlcompress.md>`__,
due to implementation intricacies it is not possible to deduce the
required buffer size from the compressed data. So the buffer must be
preallocated in advance, and unpacked data can not go over the buffer
size. This option lets you control the buffer size, both to limit
``indexer`` memory use, and to enable unpacking of really long data
fields if necessary.

Example:
^^^^^^^^

::


    unpack_mysqlcompress_maxsize = 1M

