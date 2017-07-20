Ranking overview
~~~~~~~~~~~~~~~~

Ranking (aka weighting) of the search results can be defined as a
process of computing a so-called relevance (aka weight) for every given
matched document with regards to a given query that matched it. So
relevance is in the end just a number attached to every document that
estimates how relevant the document is to the query. Search results can
then be sorted based on this number and/or some additional parameters,
so that the most sought after results would come up higher on the
results page.

There is no single standard one-size-fits-all way to rank any document
in any scenario. Moreover, there can not ever be such a way, because
relevance is *subjective*. As in, what seems relevant to you might not
seem relevant to me. Hence, in general case it's not just hard to
compute, it's theoretically impossible.

So ranking in Manticore is configurable. It has a notion of a so-called
<b>ranker</b>. A ranker can formally be defined as a function that takes
document and query as its input and produces a relevance value as
output. In layman's terms, a ranker controls exactly how (using which
specific algorithm) will Manticore assign weights to the document.

Previously, this ranking function was rigidly bound to the matching
mode. So in the legacy matching modes (that is, SPH\_MATCH\_ALL,
SPH\_MATCH\_ANY, SPH\_MATCH\_PHRASE, and SPH\_MATCH\_BOOLEAN) you can
not choose the ranker. You can only do that in the SPH\_MATCH\_EXTENDED
mode. (Which is the only mode in SphinxQL and the suggested mode in
ManticoreAPI anyway.) To choose a non-default ranker you can either use
`SetRankingMode() <../../full-text_search_query_settings/setrankingmode.md>`__
with ManticoreAPI, or `OPTION ranker <../../select_syntax.md>`__ clause in
``SELECT`` statement when using SphinxQL.

As a sidenote, legacy matching modes are internally implemented via the
unified syntax anyway. When you use one of those modes, Manticore just
internally adjusts the query and sets the associated ranker, then
executes the query using the very same unified code path.
