### sql_ranged_throttle {#sql-ranged-throttle}

Ranged query throttling period, in milliseconds. Optional, default is 0 (no throttling). Applies to SQL source types (`mysql`, `pgsql`, `mssql`) only.

Throttling can be useful when indexer imposes too much load on the database server. It causes the indexer to sleep for given amount of milliseconds once per each ranged query step. This sleep is unconditional, and is performed before the fetch query.

#### Example: {#example}

```

sql_ranged_throttle = 1000 # sleep for 1 sec before each query step

```