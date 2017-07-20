SHOW TABLES syntax
------------------

::


    SHOW TABLES [ LIKE pattern ]

SHOW TABLES statement enumerates all currently active indexes along with
their types. Existing index types are ``local``, ``distributed``,
``rt``,and ``template`` respectively. Example:

::


    mysql> SHOW TABLES;
    +-------+-------------+
    | Index | Type        |
    +-------+-------------+
    | dist1 | distributed |
    | rt    | rt          |
    | test1 | local       |
    | test2 | local       |
    +-------+-------------+
    4 rows in set (0.00 sec)

An optional LIKE clause is supported. Refer to `the section called “SHOW
META syntax” <../show_meta_syntax.md>`__ for its syntax details.

::


    mysql> SHOW TABLES LIKE '%4';
    +-------+-------------+
    | Index | Type        |
    +-------+-------------+
    | dist4 | distributed |
    +-------+-------------+
    1 row in set (0.00 sec)

