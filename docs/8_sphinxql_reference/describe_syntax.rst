DESCRIBE syntax
---------------

::


    {DESC | DESCRIBE} index [ LIKE pattern ]

DESCRIBE statement, introduced in version 2.0.1-beta, lists index
columns and their associated types. Columns are document ID, full-text
fields, and attributes. The order matches that in which fields and
attributes are expected by INSERT and REPLACE statements. As of
2.0.1-beta, column types are ``field``, ``integer``, ``timestamp``,
``ordinal``, ``bool``, ``float``, ``bigint``, ``string``, and ``mva``.
ID column will be typed either ``integer`` or ``bigint`` based on
whether the binaries were built with 32-bit or 64-bit document ID
support. Example:

::


    mysql> DESC rt;
    +---------+---------+
    | Field   | Type    |
    +---------+---------+
    | id      | integer |
    | title   | field   |
    | content | field   |
    | gid     | integer |
    +---------+---------+
    4 rows in set (0.00 sec)

Starting from version 2.1.1-beta, an optional LIKE clause is supported.
Refer to `the section called “SHOW META
syntax” <../show_meta_syntax.html>`__ for its syntax details.
