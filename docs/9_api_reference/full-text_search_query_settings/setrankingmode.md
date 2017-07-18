### SetRankingMode {#setrankingmode}

&lt;b&gt;Prototype:&lt;/b&gt; function SetRankingMode ( $ranker, $rankexpr=&quot;&quot; )

Sets ranking mode (aka ranker). Only available in SPH_MATCH_EXTENDED matching mode. Parameter must be a constant specifying one of the known rankers.

By default, in the EXTENDED matching mode Sphinx computes two factors which contribute to the final match weight. The major part is a phrase proximity value between the document text and the query. The minor part is so-called BM25 statistical function, which varies from 0 to 1 depending on the keyword frequency within document (more occurrences yield higher weight) and within the whole index (more rare keywords yield higher weight).

However, in some cases you&#039;d want to compute weight differently - or maybe avoid computing it at all for performance reasons because you&#039;re sorting the result set by something else anyway. This can be accomplished by setting the appropriate ranking mode. The list of the modes is available in [the section called “Search results ranking”](../../search_results_ranking/README.md).

`$rankexpr` argument was added in version 2.0.2-beta. It lets you specify a ranking formula to use with the [expression based ranker](../../search_results_ranking/expression_based_ranker_sphrank_expr.md), that is, when `$ranker` is set to SPH_RANK_EXPR. In all other cases, `$rankexpr` is ignored.