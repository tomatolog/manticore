sql\_range\_step
~~~~~~~~~~~~~~~~

Range query step. Optional, default is 1024. Applies to SQL source types
(``mysql``, ``pgsql``, ``mssql``) only.

Only used when `ranged
queries <../../3_indexing/sql_data_sources_mysql,_postgresql.rst#ranged-queries>`__
are enabled. The full document IDs interval fetched by
`sql\_query\_range <../../data_source_configuration_options/sqlquery_range.rst>`__
will be walked in this big steps. For example, if min and max IDs
fetched are 12 and 3456 respectively, and the step is 1000, indexer will
call
`sql\_query <../../data_source_configuration_options/sqlquery.rst>`__
several times with the following substitutions:

-  $start=12, $end=1011

-  $start=1012, $end=2011

-  $start=2012, $end=3011

-  $start=3012, $end=3456

Example:
^^^^^^^^

::


    sql_range_step = 1000

