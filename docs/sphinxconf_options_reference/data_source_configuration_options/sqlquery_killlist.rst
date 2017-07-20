sql\_query\_killlist
~~~~~~~~~~~~~~~~~~~~

Kill-list query. Optional, default is empty (no query). Applies to SQL
source types (``mysql``, ``pgsql``, ``mssql``) only.

This query is expected to return a number of 1-column rows, each
containing just the document ID. The returned document IDs are stored
within an index. Kill-list for a given index suppresses results from
*other* indexes, depending on index order in the query. The intended use
is to help implement deletions and updates on existing indexes without
rebuilding (actually even touching them), and especially to fight
phantom results problem.

Let us dissect an example. Assume we have two indexes, ‘main’ and
‘delta’. Assume that documents 2, 3, and 5 were deleted since last
reindex of ‘main’, and documents 7 and 11 were updated (ie. their text
contents were changed). Assume that a keyword ‘test’ occurred in all
these mentioned documents when we were indexing ‘main’; still occurs in
document 7 as we index ‘delta’; but does not occur in document 11 any
more. We now reindex delta and then search through both these indexes in
proper (least to most recent) order:

::


    $res = $cl->Query ( "test", "main delta" );

First, we need to properly handle deletions. The result set should not
contain documents 2, 3, or 5. Second, we also need to avoid phantom
results. Unless we do something about it, document 11 *will* appear in
search results! It will be found in ‘main’ (but not ‘delta’). And it
will make it to the final result set unless something stops it.

Kill-list, or K-list for short, is that something. Kill-list attached to
‘delta’ will suppress the specified rows from <b>all</b> the preceding
indexes, in this case just ‘main’. So to get the expected results, we
should put all the updated *and* deleted document IDs into it.

Note that in the distributed index setup, K-lists are <b>local to every
node in the cluster</b>. They are <b>not</b> get transmitted over the
network when sending queries. (Because that might be too much of an
impact when the K-list is huge.) You will need to setup a separate
per-server K-lists in that case.

Example:
^^^^^^^^

::


    sql_query_killlist = \
        SELECT id FROM documents WHERE updated_ts>=@last_reindex UNION \
        SELECT id FROM documents_deleted WHERE deleted_ts>=@last_reindex

