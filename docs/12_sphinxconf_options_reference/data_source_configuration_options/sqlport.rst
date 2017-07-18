sql\_port
~~~~~~~~~

SQL server IP port to connect to. Optional, default is 3306 for
``mysql`` source type and 5432 for ``pgsql`` type. Applies to SQL source
types (``mysql``, ``pgsql``, ``mssql``) only. Note that it depends on
`sql\_host <../../data_source_configuration_options/sqlhost.md>`__
setting whether this value will actually be used.

Example:
^^^^^^^^

::


    sql_port = 3306

