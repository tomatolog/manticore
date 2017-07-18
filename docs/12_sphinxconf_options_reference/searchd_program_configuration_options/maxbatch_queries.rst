max\_batch\_queries
~~~~~~~~~~~~~~~~~~~

Limits the amount of queries per batch. Optional, default is 32.

Makes searchd perform a sanity check of the amount of the queries
submitted in a single batch when using
`multi-queries <../../multi-queries.md>`__. Set it to 0 to skip the
check.

Example:
^^^^^^^^

::


    max_batch_queries = 256

