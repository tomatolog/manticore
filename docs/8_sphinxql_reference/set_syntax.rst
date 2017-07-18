SET syntax
----------

::


    SET [GLOBAL] server_variable_name = value
    SET [INDEX index_name] GLOBAL @user_variable_name = (int_val1 [, int_val2, ...])
    SET NAMES value
    SET @@dummy_variable = ignored_value

SET statement, introduced in version 1.10-beta, modifies a variable
value. The variable names are case-insensitive. No variable value
changes survive server restart.

SET NAMES statement and SET @@variable\_name syntax, both introduced in
version 2.0.2-beta, do nothing. They were implemented to maintain
compatibility with 3rd party MySQL client libraries, connectors, and
frameworks that may need to run this statement when connecting.

There are the following classes of the variables:

1. per-session server variable (1.10-beta and above)

2. global server variable (2.0.1-beta and above)

3. global user variable (2.0.1-beta and above)

4. global distributed variable (2.2.3-beta and above)

Global user variables are shared between concurrent sessions. Currently,
the only supported value type is the list of BIGINTs, and these
variables can only be used along with IN() for filtering purpose. The
intended usage scenario is uploading huge lists of values to ``searchd``
(once) and reusing them (many times) later, saving on network overheads.
Starting with 2.2.3-beta, global user variables might be either
transferred to all agents of distributed index or set locally in case of
local index defined at distibuted index. Example:

::


    // in session 1
    mysql> SET GLOBAL @myfilter=(2,3,5,7,11,13);
    Query OK, 0 rows affected (0.00 sec)

    // later in session 2
    mysql> SELECT * FROM test1 WHERE group_id IN @myfilter;
    +------+--------+----------+------------+-----------------+------+
    | id   | weight | group_id | date_added | title           | tag  |
    +------+--------+----------+------------+-----------------+------+
    |    3 |      1 |        2 | 1299338153 | another doc     | 15   |
    |    4 |      1 |        2 | 1299338153 | doc number four | 7,40 |
    +------+--------+----------+------------+-----------------+------+
    2 rows in set (0.02 sec)

Per-session and global server variables affect certain server settings
in the respective scope. Known per-session server variables are:

-  ``AUTOCOMMIT = {0 | 1}``
-  Whether any data modification statement should be implicitly wrapped
   by BEGIN and COMMIT. Introduced in version 1.10-beta.

-  ``COLLATION_CONNECTION = collation_name``
-  Selects the collation to be used for ORDER BY or GROUP BY on string
   values in the subsequent queries. Refer to `the section called
   “Collations” <../collations.md>`__ for a list of known collation
   names. Introduced in version 2.0.1-beta.

-  ``CHARACTER_SET_RESULTS = charset_name``
-  Does nothing; a placeholder to support frameworks, clients, and
   connectors that attempt to automatically enforce a charset when
   connecting to a Sphinx server. Introduced in version 2.0.1-beta.

-  ``SQL_AUTO_IS_NULL = value``
-  Does nothing; a placeholder to support frameworks, clients, and
   connectors that attempt to automatically enforce a charset when
   connecting to a Sphinx server. Introduced in version 2.0.2-beta.

-  ``SQL_MODE = value``
-  Does nothing; a placeholder to support frameworks, clients, and
   connectors that attempt to automatically enforce a charset when
   connecting to a Sphinx server. Introduced in version 2.0.2-beta.

-  ``PROFILING = {0 | 1}``
-  Enables query profiling in the current session. Defaults to 0. See
   also `the section called “SHOW PROFILE
   syntax” <../show_profile_syntax.md>`__. Introduced in version
   2.1.1-beta.

Known global server variables are:

-  ``QUERY_LOG_FORMAT = {plain | sphinxql}``
-  Changes the current log format. Introduced in version 2.0.1-beta.

-  ``LOG_LEVEL = {info | debug | debugv | debugvv}``
-  Changes the current log verboseness level. Introduced in version
   2.0.1-beta.

-  ``QCACHE_MAX_BYTES = &lt;value&gt;``
-  Changes the `query cache <../query_cache.md>`__ RAM use limit to a
   given value. Added in 2.3.1-beta.

-  ``QCACHE_THRESH_MSEC = &lt;value&gt;``
-  Changes the `query cache <../query_cache.md>`__ minimum wall time
   threshold to a given value. Added in 2.3.1-beta.

-  ``QCACHE_TTL_SEC = &lt;value&gt;``
-  Changes the `query cache <../query_cache.md>`__ TTL for a cached
   result to a given value. Added in 2.3.1-beta.

Examples:

::


    mysql> SET autocommit=0;
    Query OK, 0 rows affected (0.00 sec)

    mysql> SET GLOBAL query_log_format=sphinxql;
    Query OK, 0 rows affected (0.00 sec)

