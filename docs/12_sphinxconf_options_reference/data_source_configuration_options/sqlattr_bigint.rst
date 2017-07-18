sql\_attr\_bigint
~~~~~~~~~~~~~~~~~

64-bit signed integer `attribute <../../attributes.rst>`__ declaration.
Multi-value (there might be multiple attributes declared), optional.
Applies to SQL source types (``mysql``, ``pgsql``, ``mssql``) only. Note
that unlike
`sql\_attr\_uint <../../data_source_configuration_options/sqlattr_uint.rst>`__,
these values are <b>signed</b>. Introduced in version 0.9.9-rc1.

Example:
^^^^^^^^

::


    sql_attr_bigint = my_bigint_id

