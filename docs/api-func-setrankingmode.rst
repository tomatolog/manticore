.. raw:: html

   <div class="navheader">

9.3.2. SetRankingMode
`Prev <api-func-setmatchmode.html>`__ 
9.3. Full-text search query settings
 `Next <api-func-setsortmode.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect2">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 9.3.2. SetRankingMode
   :name: setrankingmode
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function SetRankingMode ( $ranker, $rankexpr=“” )

Sets ranking mode (aka ranker). Only available in SPH\_MATCH\_EXTENDED
matching mode. Parameter must be a constant specifying one of the known
rankers.

By default, in the EXTENDED matching mode Sphinx computes two factors
which contribute to the final match weight. The major part is a phrase
proximity value between the document text and the query. The minor part
is so-called BM25 statistical function, which varies from 0 to 1
depending on the keyword frequency within document (more occurrences
yield higher weight) and within the whole index (more rare keywords
yield higher weight).

However, in some cases you’d want to compute weight differently - or
maybe avoid computing it at all for performance reasons because you’re
sorting the result set by something else anyway. This can be
accomplished by setting the appropriate ranking mode. The list of the
modes is available in `Section 5.4, “Search results
ranking” <weighting.html>`__.

``$rankexpr`` argument was added in version 2.0.2-beta. It lets you
specify a ranking formula to use with the `expression based
ranker <expression-ranker.html>`__, that is, when ``$ranker`` is set to
SPH\_RANK\_EXPR. In all other cases, ``$rankexpr`` is ignored.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+-------------------------------------------------------+-----------------------------------------+
| `Prev <api-func-setmatchmode.html>`__    | `Up <api-funcgroup-fulltext-query-settings.html>`__   |  `Next <api-func-setsortmode.html>`__   |
+------------------------------------------+-------------------------------------------------------+-----------------------------------------+
| 9.3.1. SetMatchMode                      | `Home <index.html>`__                                 |  9.3.3. SetSortMode                     |
+------------------------------------------+-------------------------------------------------------+-----------------------------------------+

.. raw:: html

   </div>
