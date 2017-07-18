### query_log_format {#query-log-format}

Query log format. Optional, allowed values are &#039;plain&#039; and &#039;sphinxql&#039;, default is &#039;plain&#039;. Introduced in version 2.0.1-beta.

Starting with version 2.0.1-beta, two different log formats are supported. The default one logs queries in a custom text format. The new one logs valid SphinxQL statements. This directive allows to switch between the two formats on search daemon startup. The log format can also be altered on the fly, using `SET GLOBAL query_log_format=sphinxql` syntax. Refer to [the section called “`searchd` query log formats”](../../searchd_query_log_formats/README.md) for more discussion and format details.

#### Example: {#example}

```

query_log_format = sphinxql

```