### sql_sock {#sql-sock}

UNIX socket name to connect to for local SQL servers. Optional, default value is empty (use client library default settings). Applies to SQL source types (`mysql`, `pgsql`, `mssql`) only.

On Linux, it would typically be `/var/lib/mysql/mysql.sock`. On FreeBSD, it would typically be `/tmp/mysql.sock`. Note that it depends on [sql_host](../../data_source_configuration_options/sqlhost.md) setting whether this value will actually be used.

#### Example: {#example}

```

sql_sock = /tmp/mysql.sock

```