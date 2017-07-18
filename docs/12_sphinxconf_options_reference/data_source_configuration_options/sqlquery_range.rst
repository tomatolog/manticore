sql\_query\_range
~~~~~~~~~~~~~~~~~

Range query setup. Optional, default is empty. Applies to SQL source
types (``mysql``, ``pgsql``, ``mssql``) only.

Setting this option enables ranged document fetch queries (see `the
section called “Ranged
queries” <../../3_indexing/sql_data_sources_mysql,_postgresql.md#ranged-queries>`__).
Ranged queries are useful to avoid notorious MyISAM table locks when
indexing lots of data. (They also help with other less notorious issues,
such as reduced performance caused by big result sets, or additional
resources consumed by InnoDB to serialize big read transactions.)

The query specified in this option must fetch min and max document IDs
that will be used as range boundaries. It must return exactly two
integer fields, min ID first and max ID second; the field names are
ignored.

When ranged queries are enabled,
`sql\_query <../../data_source_configuration_options/sqlquery.md>`__
will be required to contain ``$start`` and ``$end`` macros (because it
obviously would be a mistake to index the whole table many times over).
Note that the intervals specified by ``$start``..\ ``$end`` will not
overlap, so you should <b>not</b> remove document IDs that are exactly
equal to ``$start`` or ``$end`` from your query. The example in `the
section called “Ranged
queries” <../../3_indexing/sql_data_sources_mysql,_postgresql.md#ranged-queries>`__)
illustrates that; note how it uses greater-or-equal and less-or-equal
comparisons.

Example:
^^^^^^^^

::


    sql_query_range = SELECT MIN(id),MAX(id) FROM documents

