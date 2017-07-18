subtree\_docs\_cache
~~~~~~~~~~~~~~~~~~~~

Max common subtree document cache size, per-query. Optional, default is
0 (disabled).

Limits RAM usage of a common subtree optimizer (see `the section called
“Multi-queries” <../../multi-queries.rst>`__). At most this much RAM will
be spent to cache document entries per each query. Setting the limit to
0 disables the optimizer.

Example:
^^^^^^^^

::


    subtree_docs_cache = 8M

