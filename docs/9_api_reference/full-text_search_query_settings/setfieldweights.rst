SetFieldWeights
~~~~~~~~~~~~~~~

<b>Prototype:</b> function SetFieldWeights ( $weights )

Binds per-field weights by name. Parameter must be a hash (associative
array) mapping string field names to integer weights.

Match ranking can be affected by per-field weights. For instance, see
`the section called “Search results
ranking” <../../search_results_ranking/README.md>`__ for an explanation
how phrase proximity ranking is affected. This call lets you specify
what non-default weights to assign to different full-text fields.

The weights must be positive 32-bit integers. The final weight will be a
32-bit integer too. Default weight value is 1. Unknown field names will
be silently ignored.

There is no enforced limit on the maximum weight value at the moment.
However, beware that if you set it too high you can start hitting 32-bit
wraparound issues. For instance, if you set a weight of 10,000,000 and
search in extended mode, then maximum possible weight will be equal to
10 million (your weight) by 1 thousand (internal BM25 scaling factor,
see `the section called “Search results
ranking” <../../search_results_ranking/README.md>`__) by 1 or more
(phrase proximity rank). The result is at least 10 billion that does not
fit in 32 bits and will be wrapped around, producing unexpected results.
