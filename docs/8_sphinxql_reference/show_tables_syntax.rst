SHOW TABLES syntax
------------------

::


    SHOW TABLES [ LIKE pattern ]

SHOW TABLES statement, introduced in version 2.0.1-beta, enumerates all
currently active indexes along with their types. As of 2.0.1-beta,
existing index types are ``local``, ``distributed``, and ``rt``
respectively. Example:

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

Starting from version 2.1.1-beta, an optional LIKE clause is supported.
Refer to `the section called “SHOW META
syntax” <../show_meta_syntax.html>`__ for its syntax details.

::


    mysql> SHOW TABLES LIKE '%4';
    +-------+-------------+
    | Index | Type        |
    +-------+-------------+
    | dist4 | distributed |
    +-------+-------------+
    1 row in set (0.00 sec)

