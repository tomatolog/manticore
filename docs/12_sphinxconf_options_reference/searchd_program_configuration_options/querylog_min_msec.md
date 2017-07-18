### query_log_min_msec {#query-log-min-msec}

Limit (in milliseconds) that prevents the query from being written to the query log. Optional, default is 0 (all queries are written to the query log). This directive specifies that only queries with execution times that exceed the specified limit will be logged.