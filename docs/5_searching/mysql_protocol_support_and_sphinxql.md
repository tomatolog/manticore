## MySQL protocol support and SphinxQL {#mysql-protocol-support-and-sphinxql}

Starting with version 0.9.9-rc2, Sphinx searchd daemon supports MySQL binary network protocol and can be accessed with regular MySQL API. For instance, &#039;mysql&#039; CLI client program works well. Here&#039;s an example of querying Sphinx using MySQL client:

```

$ mysql -P 9306
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 1
Server version: 0.9.9-dev (r1734)

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> SELECT * FROM test1 WHERE MATCH('test')
    -> ORDER BY group_id ASC OPTION ranker=bm25;
+------+--------+----------+------------+
| id   | weight | group_id | date_added |
+------+--------+----------+------------+
|    4 |   1442 |        2 | 1231721236 |
|    2 |   2421 |      123 | 1231721236 |
|    1 |   2421 |      456 | 1231721236 |
+------+--------+----------+------------+
3 rows in set (0.00 sec)

```

Note that mysqld was not even running on the test machine. Everything was handled by searchd itself.

The new access method is supported _in addition_ to native APIs which all still work perfectly well. In fact, both access methods can be used at the same time. Also, native API is still the default access method. MySQL protocol support needs to be additionally configured. This is a matter of 1-line config change, adding a new [listener](../searchd_program_configuration_options/listen.md) with mysql41 specified as a protocol:

```

listen = localhost:9306:mysql41

```

Just supporting the protocol and not the SQL syntax would be useless so Sphinx now also supports a subset of SQL that we dubbed SphinxQL. It supports the standard querying all the index types with SELECT, modifying RT indexes with INSERT, REPLACE, and DELETE, and much more. Full SphinxQL reference is available in [Chapter 8, _SphinxQL reference_](../8_sphinxql_reference/README.md).