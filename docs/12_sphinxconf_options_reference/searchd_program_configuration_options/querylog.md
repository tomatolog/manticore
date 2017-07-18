### query_log {#query-log}

Query log file name. Optional, default is empty (do not log queries). All search queries will be logged in this file. The format is described in [the section called “`searchd` query log formats”](../../searchd_query_log_formats/README.md).

In case of &#039;plain&#039; format, you can use the &#039;syslog&#039; as the path to the log file. In this case all search queries will be sent to syslog daemon with LOG_INFO priority, prefixed with &#039;[query]&#039; instead of timestamp. To use the syslog option the sphinx must be configured &#039;--with-syslog&#039; on building.

#### Example: {#example}

```

query_log = /var/log/query.log

```