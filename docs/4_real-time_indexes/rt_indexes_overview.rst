RT indexes overview
-------------------

RT indexes should be declared in ``sphinx.conf``, just as every other
index type. Notable differences from the regular, disk-based indexes are
that a) data sources are not required and ignored, and b) you should
explicitly enumerate all the text fields, not just attributes. Here's an
example:

Example 4.1. RT index declaration
                                 

::


    index rt
    {
        type = rt
        path = /usr/local/sphinx/data/rt
        rt_field = title
        rt_field = content
        rt_attr_uint = gid
    }

As of 2.0.1-beta and above, RT indexes are production quality, despite a
few missing features.

RT index can be accessed using MySQL protocol. INSERT, REPLACE, DELETE,
and SELECT statements against RT index are supported. For instance, this
is an example session with the sample index above:

::


    $ mysql -h 127.0.0.1 -P 9306
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 1
    Server version: 1.10-dev (r2153)

    Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

    mysql> INSERT INTO rt VALUES ( 1, 'first record', 'test one', 123 );
    Query OK, 1 row affected (0.05 sec)

    mysql> INSERT INTO rt VALUES ( 2, 'second record', 'test two', 234 );
    Query OK, 1 row affected (0.00 sec)

    mysql> SELECT * FROM rt;
    +------+--------+------+
    | id   | weight | gid  |
    +------+--------+------+
    |    1 |      1 |  123 |
    |    2 |      1 |  234 |
    +------+--------+------+
    2 rows in set (0.02 sec)

    mysql> SELECT * FROM rt WHERE MATCH('test');
    +------+--------+------+
    | id   | weight | gid  |
    +------+--------+------+
    |    1 |   1643 |  123 |
    |    2 |   1643 |  234 |
    +------+--------+------+
    2 rows in set (0.01 sec)

    mysql> SELECT * FROM rt WHERE MATCH('@title test');
    Empty set (0.00 sec)

Both partial and batch INSERT syntaxes are supported, ie. you can
specify a subset of columns, and insert several rows at a time.
Deletions are also possible using DELETE statement; the only currently
supported syntax is DELETE FROM <index> WHERE id=<id>. REPLACE is also
supported, enabling you to implement updates.

::


    mysql> INSERT INTO rt ( id, title ) VALUES ( 3, 'third row' ), ( 4, 'fourth entry' );
    Query OK, 2 rows affected (0.01 sec)

    mysql> SELECT * FROM rt;
    +------+--------+------+
    | id   | weight | gid  |
    +------+--------+------+
    |    1 |      1 |  123 |
    |    2 |      1 |  234 |
    |    3 |      1 |    0 |
    |    4 |      1 |    0 |
    +------+--------+------+
    4 rows in set (0.00 sec)

    mysql> DELETE FROM rt WHERE id=2;
    Query OK, 0 rows affected (0.00 sec)

    mysql> SELECT * FROM rt WHERE MATCH('test');
    +------+--------+------+
    | id   | weight | gid  |
    +------+--------+------+
    |    1 |   1500 |  123 |
    +------+--------+------+
    1 row in set (0.00 sec)

    mysql> INSERT INTO rt VALUES ( 1, 'first record on steroids', 'test one', 123 );
    ERROR 1064 (42000): duplicate id '1'

    mysql> REPLACE INTO rt VALUES ( 1, 'first record on steroids', 'test one', 123 );
    Query OK, 1 row affected (0.01 sec)

    mysql> SELECT * FROM rt WHERE MATCH('steroids');
    +------+--------+------+
    | id   | weight | gid  |
    +------+--------+------+
    |    1 |   1500 |  123 |
    +------+--------+------+
    1 row in set (0.01 sec)

Data stored in RT index should survive clean shutdown. When binary
logging is enabled, it should also survive crash and/or dirty shutdown,
and recover on subsequent startup.
