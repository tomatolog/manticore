sql\_query\_post
~~~~~~~~~~~~~~~~

Post-fetch query. Optional, default value is empty. Applies to SQL
source types (``mysql``, ``pgsql``, ``mssql``) only.

This query is executed immediately after
`sql\_query <../../data_source_configuration_options/sqlquery.rst>`__
completes successfully. When post-fetch query produces errors, they are
reported as warnings, but indexing is <b>not</b> terminated. It's result
set is ignored. Note that indexing is <b>not</b> yet completed at the
point when this query gets executed, and further indexing still may
fail. Therefore, any permanent updates should not be done from here. For
instance, updates on helper table that permanently change the last
successfully indexed ID should not be run from post-fetch query; they
should be run from `post-index
query <../../data_source_configuration_options/sqlquery_post_index.rst>`__
instead.

Example:
^^^^^^^^

::


    sql_query_post = DROP TABLE my_tmp_table

