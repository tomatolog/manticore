### max_batch_queries {#max-batch-queries}

Limits the amount of queries per batch. Optional, default is 32.

Makes searchd perform a sanity check of the amount of the queries submitted in a single batch when using [multi-queries](../../multi-queries.md). Set it to 0 to skip the check.

#### Example: {#example}

```

max_batch_queries = 256

```