SetRankingMode
~~~~~~~~~~~~~~

<b>Prototype:</b> function SetRankingMode ( $ranker, $rankexpr=“” )

Sets ranking mode (aka ranker). Only available in SPH\_MATCH\_EXTENDED
matching mode. Parameter must be a constant specifying one of the known
rankers.

By default, in the EXTENDED matching mode Manticore computes two factors
which contribute to the final match weight. The major part is a phrase
proximity value between the document text and the query. The minor part
is so-called BM25 statistical function, which varies from 0 to 1
depending on the keyword frequency within document (more occurrences
yield higher weight) and within the whole index (more rare keywords
yield higher weight).

However, in some cases you'd want to compute weight differently - or
maybe avoid computing it at all for performance reasons because you're
sorting the result set by something else anyway. This can be
accomplished by setting the appropriate ranking mode. The list of the
modes is available in `the section called “Search results
ranking” <../../search_results_ranking/README.md>`__.

``$rankexpr`` argument lets you specify a ranking formula to use with
the `expression based
ranker <../../search_results_ranking/expression_based_ranker_sphrank_expr.md>`__,
that is, when ``$ranker`` is set to SPH\_RANK\_EXPR. In all other cases,
``$rankexpr`` is ignored.
