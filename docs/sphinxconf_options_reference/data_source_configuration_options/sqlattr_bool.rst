sql\_attr\_bool
~~~~~~~~~~~~~~~

Boolean `attribute <../../attributes.md>`__ declaration. Multi-value
(there might be multiple attributes declared), optional. Applies to SQL
source types (``mysql``, ``pgsql``, ``mssql``) only. Equivalent to
`sql\_attr\_uint <../../data_source_configuration_options/sqlattr_uint.md>`__
declaration with a bit count of 1.

Example:
^^^^^^^^

::


    sql_attr_bool = is_deleted # will be packed to 1 bit

