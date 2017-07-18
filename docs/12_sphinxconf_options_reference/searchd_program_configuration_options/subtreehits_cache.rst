subtree\_hits\_cache
~~~~~~~~~~~~~~~~~~~~

Max common subtree hit cache size, per-query. Optional, default is 0
(disabled).

Limits RAM usage of a common subtree optimizer (see `the section called
“Multi-queries” <../../multi-queries.rst>`__). At most this much RAM will
be spent to cache keyword occurrences (hits) per each query. Setting the
limit to 0 disables the optimizer.

Example:
^^^^^^^^

::


    subtree_hits_cache = 16M

