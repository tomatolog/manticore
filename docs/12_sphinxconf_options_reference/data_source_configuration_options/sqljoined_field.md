### sql_joined_field {#sql-joined-field}

Joined/payload field fetch query. Multi-value, optional, default is empty list of queries. Applies to SQL source types (`mysql`, `pgsql`, `mssql`) only.

`sql_joined_field` lets you use two different features: joined fields, and payloads (payload fields). It&#039;s syntax is as follows:

```

sql_joined_field = FIELD-NAME 'from'  ( 'query' | 'payload-query' \
    | 'ranged-query' ); QUERY [ ; RANGE-QUERY ]

```

where

*   FIELD-NAME is a joined/payload field name;

*   QUERY is an SQL query that must fetch values to index.

*   RANGE-QUERY is an optional SQL query that fetches a range of values to index. (Added in version 2.0.1-beta.)

&lt;b&gt;Joined fields&lt;/b&gt; let you avoid JOIN and/or GROUP_CONCAT statements in the main document fetch query (sql_query). This can be useful when SQL-side JOIN is slow, or needs to be offloaded on Sphinx side, or simply to emulate MySQL-specific GROUP_CONCAT functionality in case your database server does not support it.

The query must return exactly 2 columns: document ID, and text to append to a joined field. Document IDs can be duplicate, but they &lt;b&gt;must&lt;/b&gt; be in ascending order. All the text rows fetched for a given ID will be concatenated together, and the concatenation result will be indexed as the entire contents of a joined field. Rows will be concatenated in the order returned from the query, and separating whitespace will be inserted between them. For instance, if joined field query returns the following rows:

```

( 1, 'red' )
( 1, 'right' )
( 1, 'hand' )
( 2, 'mysql' )
( 2, 'sphinx' )

```

then the indexing results would be equivalent to that of adding a new text field with a value of &#039;red right hand&#039; to document 1 and &#039;mysql sphinx&#039; to document 2.

Joined fields are only indexed differently. There are no other differences between joined fields and regular text fields.

Starting with 2.0.1-beta, &lt;b&gt;ranged queries&lt;/b&gt; can be used when a single query is not efficient enough or does not work because of the database driver limitations. It works similar to the ranged queries in the main indexing loop, see [the section called “Ranged queries”](../../3_indexing/sql_data_sources_mysql,_postgresql.md#ranged-queries). The range will be queried for and fetched upfront once, then multiple queries with different `$start` and `$end` substitutions will be run to fetch the actual data.

&lt;b&gt;Payloads&lt;/b&gt; let you create a special field in which, instead of keyword positions, so-called user payloads are stored. Payloads are custom integer values attached to every keyword. They can then be used in search time to affect the ranking.

The payload query must return exactly 3 columns: document ID; keyword; and integer payload value. Document IDs can be duplicate, but they &lt;b&gt;must&lt;/b&gt; be in ascending order. Payloads must be unsigned integers within 24-bit range, ie. from 0 to 16777215\. For reference, payloads are currently internally stored as in-field keyword positions, but that is not guaranteed and might change in the future.

Currently, the only method to account for payloads is to use SPH_RANK_PROXIMITY_BM25 ranker. On indexes with payload fields, it will automatically switch to a variant that matches keywords in those fields, computes a sum of matched payloads multiplied by field weights, and adds that sum to the final rank.

#### Example: {#example}

```

sql_joined_field = \
    tagstext from query; \
    SELECT docid, CONCAT('tag',tagid) FROM tags ORDER BY docid ASC

sql_joined_field = bigint tag from ranged-query; \
    SELECT id, tag FROM tags WHERE id>=$start AND id<=$end ORDER BY id ASC; \
    SELECT MIN(id), MAX(id) FROM tags

```