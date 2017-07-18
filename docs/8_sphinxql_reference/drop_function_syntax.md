## DROP FUNCTION syntax {#drop-function-syntax}

```

DROP FUNCTION udf_name

```

DROP FUNCTION statement, introduced in version 2.0.1-beta, deinstalls a [user-defined function (UDF)](../sphinx_udfs_user_defined_functions.md) with the given name. On success, the function is no longer available for use in subsequent queries. Pending concurrent queries will not be affected and the library unload, if necessary, will be postponed until those queries complete. Example:

```

mysql> DROP FUNCTION avgmva;
Query OK, 0 rows affected (0.00 sec)

```