AddQuery
~~~~~~~~

<b>Prototype:</b> function AddQuery ( $query, $index=“\*“, $comment=”" )

Adds additional query with current settings to multi-query batch.
``$query`` is a query string. ``$index`` is an index name (or names)
string. Additionally if provided, the contents of ``$comment`` are sent
to the query log, marked in square brackets, just before the search
terms, which can be very useful for debugging. Currently, this is
limited to 128 characters. Returns index to results array returned from
`RunQueries() <../../querying/runqueries.html>`__.

Batch queries (or multi-queries) enable ``searchd`` to perform internal
optimizations if possible. They also reduce network connection overheads
and search process creation overheads in all cases. They do not result
in any additional overheads compared to simple queries. Thus, if you run
several different queries from your web page, you should always consider
using multi-queries.

For instance, running the same full-text query but with different
sorting or group-by settings will enable ``searchd`` to perform
expensive full-text search and ranking operation only once, but compute
multiple group-by results from its output.

This can be a big saver when you need to display not just plain search
results but also some per-category counts, such as the amount of
products grouped by vendor. Without multi-query, you would have to run
several queries which perform essentially the same search and retrieve
the same matches, but create result sets differently. With multi-query,
you simply pass all these queries in a single batch and Sphinx optimizes
the redundant full-text search internally.

``AddQuery()`` internally saves full current settings state along with
the query, and you can safely change them afterwards for subsequent
``AddQuery()`` calls. Already added queries will not be affected;
there's actually no way to change them at all. Here's an example:

::


    $cl->SetSortMode ( SPH_SORT_RELEVANCE );
    $cl->AddQuery ( "hello world", "documents" );

    $cl->SetSortMode ( SPH_SORT_ATTR_DESC, "price" );
    $cl->AddQuery ( "ipod", "products" );

    $cl->AddQuery ( "harry potter", "books" );

    $results = $cl->RunQueries ();

With the code above, 1st query will search for “hello world” in
“documents” index and sort results by relevance, 2nd query will search
for “ipod” in “products” index and sort results by price, and 3rd query
will search for “harry potter” in “books” index while still sorting by
price. Note that 2nd ``SetSortMode()`` call does not affect the f.html
query (because it's already added) but affects both other subsequent
queries.

Additionally, any filters set up before an ``AddQuery()`` will fall
through to subsequent queries. So, if ``SetFilter()`` is called before
the f.html query, the same filter will be in place for the second (and
subsequent) queries batched through ``AddQuery()`` unless you call
``ResetFilters()`` f.html. Alternatively, you can add additional filters
as well.

This would also be true for grouping options and sorting options; no
current sorting, filtering, and grouping settings are affected by this
call; so subsequent queries will reuse current query settings.

``AddQuery()`` returns an index into an array of results that will be
returned from ``RunQueries()`` call. It is simply a sequentially
increasing 0-based integer, ie. f.html call will return 0, second will
return 1, and so on. Just a small helper so you won't have to track the
indexes manually if you need then.
