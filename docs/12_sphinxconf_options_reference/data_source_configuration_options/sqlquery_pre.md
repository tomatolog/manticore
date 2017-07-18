### sql_query_pre {#sql-query-pre}

Pre-fetch query, or pre-query. Multi-value, optional, default is empty list of queries. Applies to SQL source types (`mysql`, `pgsql`, `mssql`) only.

Multi-value means that you can specify several pre-queries. They are executed before [the main fetch query](../../data_source_configuration_options/sqlquery.md), and they will be executed exactly in order of appearance in the configuration file. Pre-query results are ignored.

Pre-queries are useful in a lot of ways. They are used to setup encoding, mark records that are going to be indexed, update internal counters, set various per-connection SQL server options and variables, and so on.

Perhaps the most frequent pre-query usage is to specify the encoding that the server will use for the rows it returns. Note that Sphinx accepts only UTF-8 texts. Two MySQL specific examples of setting the encoding are:

```

sql_query_pre = SET CHARACTER_SET_RESULTS=utf8
sql_query_pre = SET NAMES utf8

```

Also specific to MySQL sources, it is useful to disable query cache (for indexer connection only) in pre-query, because indexing queries are not going to be re-run frequently anyway, and there&#039;s no sense in caching their results. That could be achieved with:

```

sql_query_pre = SET SESSION query_cache_type=OFF

```

#### Example: {#example}

```

sql_query_pre = SET NAMES utf8
sql_query_pre = SET SESSION query_cache_type=OFF

```