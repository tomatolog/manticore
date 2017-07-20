sql\_query\_post\_index
~~~~~~~~~~~~~~~~~~~~~~~

Post-index query. Optional, default value is empty. Applies to SQL
source types (``mysql``, ``pgsql``, ``mssql``) only.

This query is executed when indexing is fully and successfully
completed. If this query produces errors, they are reported as warnings,
but indexing is <b>not</b> terminated. It's result set is ignored.
``$maxid`` macro can be used in its text; it will be expanded to maximum
document ID which was actually fetched from the database during
indexing. If no documents were indexed, $maxid will be expanded to 0.

Example:
^^^^^^^^

::


    sql_query_post_index = REPLACE INTO counters ( id, val ) \
        VALUES ( 'max_indexed_id', $maxid )

