### sql_query_killlist {#sql-query-killlist}

Kill-list query. Optional, default is empty (no query). Applies to SQL source types (`mysql`, `pgsql`, `mssql`) only. Introduced in version 0.9.9-rc1.

This query is expected to return a number of 1-column rows, each containing just the document ID. The returned document IDs are stored within an index. Kill-list for a given index suppresses results from _other_ indexes, depending on index order in the query. The intended use is to help implement deletions and updates on existing indexes without rebuilding (actually even touching them), and especially to fight phantom results problem.

Let us dissect an example. Assume we have two indexes, &#039;main&#039; and &#039;delta&#039;. Assume that documents 2, 3, and 5 were deleted since last reindex of &#039;main&#039;, and documents 7 and 11 were updated (ie. their text contents were changed). Assume that a keyword &#039;test&#039; occurred in all these mentioned documents when we were indexing &#039;main&#039;; still occurs in document 7 as we index &#039;delta&#039;; but does not occur in document 11 any more. We now reindex delta and then search through both these indexes in proper (least to most recent) order:

```

$res = $cl->Query ( "test", "main delta" );

```

First, we need to properly handle deletions. The result set should not contain documents 2, 3, or 5\. Second, we also need to avoid phantom results. Unless we do something about it, document 11 _will_ appear in search results! It will be found in &#039;main&#039; (but not &#039;delta&#039;). And it will make it to the final result set unless something stops it.

Kill-list, or K-list for short, is that something. Kill-list attached to &#039;delta&#039; will suppress the specified rows from &lt;b&gt;all&lt;/b&gt; the preceding indexes, in this case just &#039;main&#039;. So to get the expected results, we should put all the updated _and_ deleted document IDs into it.

Note that in the distributed index setup, K-lists are &lt;b&gt;local to every node in the cluster&lt;/b&gt;. They are &lt;b&gt;not&lt;/b&gt; get transmitted over the network when sending queries. (Because that might be too much of an impact when the K-list is huge.) You will need to setup a separate per-server K-lists in that case.

#### Example: {#example}

```

sql_query_killlist = \
    SELECT id FROM documents WHERE updated_ts>=@last_reindex UNION \
    SELECT id FROM documents_deleted WHERE deleted_ts>=@last_reindex

```