Available built-in rankers
~~~~~~~~~~~~~~~~~~~~~~~~~~

Sphinx ships with a number of built-in rankers suited for different
purposes. A number of them uses two factors, phrase proximity (aka LCS)
and BM25. Phrase proximity works on the keyword positions, while BM25
works on the keyword frequencies. Basically, the better the degree of
the phrase match between the document body and the query, the higher is
the phrase proximity (it maxes out when the document contains the entire
query as a verbatim quote). And BM25 is higher when the document
contains more rare words. We'll save the detailed discussion for later.

Currently implemented rankers are:

-  SPH\_RANK\_PROXIMITY\_BM25, the default ranking mode that uses and
   combines both phrase proximity and BM25 ranking.

-  SPH\_RANK\_BM25, statistical ranking mode which uses BM25 ranking
   only (similar to most other full-text engines). This mode is faster
   but may result in worse quality on queries which contain more than 1
   keyword.

-  SPH\_RANK\_NONE, no ranking mode. This mode is obviously the fastest.
   A weight of 1 is assigned to all matches. This is sometimes called
   boolean searching that just matches the documents but does not rank
   them.

-  SPH\_RANK\_WORDCOUNT, ranking by the keyword occurrences count. This
   ranker computes the per-field keyword occurrence counts, then
   multiplies them by field weights, and sums the resulting values.

-  SPH\_RANK\_PROXIMITY, added in version 0.9.9-rc1, returns raw phrase
   proximity value as a result. This mode is internally used to emulate
   SPH\_MATCH\_ALL queries.

-  SPH\_RANK\_MATCHANY, added in version 0.9.9-rc1, returns rank as it
   was computed in SPH\_MATCH\_ANY mode earlier, and is internally used
   to emulate SPH\_MATCH\_ANY queries.

-  SPH\_RANK\_FIELDMASK, added in version 0.9.9-rc2, returns a 32-bit
   mask with N-th bit corresponding to N-th fulltext field, numbering
   from 0. The bit will only be set when the respective field has any
   keyword occurrences satisfying the query.

-  SPH\_RANK\_SPH04, added in version 1.10-beta, is generally based on
   the default SPH\_RANK\_PROXIMITY\_BM25 ranker, but additionally
   boosts the matches when they occur in the very beginning or the very
   end of a text field. Thus, if a field equals the exact query, SPH04
   should rank it higher than a field that contains the exact query but
   is not equal to it. (For instance, when the query is “Hyde Park”, a
   document entitled “Hyde Park” should be ranked higher than a one
   entitled “Hyde Park, London” or “The Hyde Park Cafe”.)

-  SPH\_RANK\_EXPR, added in version 2.0.2-beta, lets you specify the
   ranking formula in run time. It exposes a number of internal text
   factors and lets you define how the final weight should be computed
   from those factors. You can find more details about its syntax and a
   reference available factors in a subsection below.

You should specify the ``SPH_RANK_`` prefix and use capital letters only
when using the
`SetRankingMode() <../../full-text_search_query_settings/setrankingmode.md>`__
call from the SphinxAPI. The API ports expose these as global constants.
Using SphinxQL syntax, the prefix should be omitted and the ranker name
is case insensitive. Example:

::


    // SphinxAPI
    $client->SetRankingMode ( SPH_RANK_SPH04 );

    // SphinxQL
    mysql_query ( "SELECT ... OPTION ranker=sph04" );

Legacy matching modes rankers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Legacy matching modes automatically select a ranker as follows:

-  SPH\_MATCH\_ALL uses SPH\_RANK\_PROXIMITY ranker;

-  SPH\_MATCH\_ANY uses SPH\_RANK\_MATCHANY ranker;

-  SPH\_MATCH\_PHRASE uses SPH\_RANK\_PROXIMITY ranker;

-  SPH\_MATCH\_BOOLEAN uses SPH\_RANK\_NONE ranker.
