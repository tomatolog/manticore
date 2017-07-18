sql\_attr\_uint
~~~~~~~~~~~~~~~

Unsigned integer `attribute <../../attributes.html>`__ declaration.
Multi-value (there might be multiple attributes declared), optional.
Applies to SQL source types (``mysql``, ``pgsql``, ``mssql``) only.

The column value should fit into 32-bit unsigned integer range. Values
outside this range will be accepted but wrapped around. For instance, -1
will be wrapped around to 2^32-1 or 4,294,967,295.

You can specify bit count for integer attributes by appending
‘:BITCOUNT’ to attribute name (see example below). Attributes with less
than default 32-bit size, or bitfields, perform slower. But they require
less RAM when using `extern
storage <../../index_configuration_options/docinfo.html>`__: such
bitfields are packed together in 32-bit chunks in ``.spa`` attribute
data file. Bit size settings are ignored if using `inline
storage <../../index_configuration_options/docinfo.html>`__.

Example:
^^^^^^^^

::


    sql_attr_uint = group_id
    sql_attr_uint = forum_id:9 # 9 bits for forum_id

