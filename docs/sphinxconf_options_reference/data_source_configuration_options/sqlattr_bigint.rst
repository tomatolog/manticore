sql\_attr\_bigint
~~~~~~~~~~~~~~~~~

64-bit signed integer `attribute <../../attributes.md>`__ declaration.
Multi-value (there might be multiple attributes declared), optional.
Applies to SQL source types (``mysql``, ``pgsql``, ``mssql``) only. Note
that unlike
`sql\_attr\_uint <../../data_source_configuration_options/sqlattr_uint.md>`__,
these values are <b>signed</b>.

Example:
^^^^^^^^

::


    sql_attr_bigint = my_bigint_id

