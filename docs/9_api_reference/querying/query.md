### Query {#query}

&lt;b&gt;Prototype:&lt;/b&gt; function Query ( $query, $index=&quot;*&quot;, $comment=&quot;&quot; )

Connects to `searchd` server, runs given search query with current settings, obtains and returns the result set.

`$query` is a query string. `$index` is an index name (or names) string. Returns false and sets `GetLastError()` message on general error. Returns search result set on success. Additionally, the contents of `$comment` are sent to the query log, marked in square brackets, just before the search terms, which can be very useful for debugging. Currently, the comment is limited to 128 characters.

Default value for `$index` is `&quot;*&quot;` that means to query all local indexes. Characters allowed in index names include Latin letters (a-z), numbers (0-9) and underscore (_); everything else is considered a separator. Note that index name should not start with underscore character. Therefore, all of the following samples calls are valid and will search the same two indexes:

```

$cl->Query ( "test query", "main delta" );
$cl->Query ( "test query", "main;delta" );
$cl->Query ( "test query", "main, delta" );

```

Index specification order matters. If document with identical IDs are found in two or more indexes, weight and attribute values from the very last matching index will be used for sorting and returning to client (unless explicitly overridden with [SetIndexWeights()](../../full-text_search_query_settings/setindexweights.md)). Therefore, in the example above, matches from &quot;delta&quot; index will always win over matches from &quot;main&quot;.

On success, `Query()` returns a result set that contains some of the found matches (as requested by [SetLimits()](../../general_query_settings/setlimits.md)) and additional general per-query statistics. The result set is a hash (PHP specific; other languages might utilize other structures instead of hash) with the following keys and values:

*   &quot;matches&quot;:
*   Hash which maps found document IDs to another small hash containing document weight and attribute values (or an array of the similar small hashes if [SetArrayResult()](../../general_api_functions/setarrayresult.md) was enabled).

*   &quot;total&quot;:
*   Total amount of matches retrieved _on server_ (ie. to the server side result set) by this query. You can retrieve up to this amount of matches from server for this query text with current query settings.

*   &quot;total_found&quot;:
*   Total amount of matching documents in index (that were found and processed on server).

*   &quot;words&quot;:
*   Hash which maps query keywords (case-folded, stemmed, and otherwise processed) to a small hash with per-keyword statistics (&quot;docs&quot;, &quot;hits&quot;).

*   &quot;error&quot;:
*   Query error message reported by `searchd` (string, human readable). Empty if there were no errors.

*   &quot;warning&quot;:
*   Query warning message reported by `searchd` (string, human readable). Empty if there were no warnings.

It should be noted that `Query()` carries out the same actions as `AddQuery()` and `RunQueries()` without the intermediate steps; it is analogous to a single `AddQuery()` call, followed by a corresponding `RunQueries()`, then returning the first array element of matches (from the first, and only, query.)