DESCRIBE syntax
---------------

::


    {DESC | DESCRIBE} index [ LIKE pattern ]

DESCRIBE statement lists index columns and their associated types.
Columns are document ID, full-text fields, and attributes. The order
matches that in which fields and attributes are expected by INSERT and
REPLACE statements. Column types are ``field``, ``integer``,
``timestamp``, ``ordinal``, ``bool``, ``float``, ``bigint``, ``string``,
and ``mva``. ID column will be typed either ``integer`` or ``bigint``
based on whether the binaries were built with 32-bit or 64-bit document
ID support. Example:

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

An optional LIKE clause is supported. Refer to `the section called “SHOW
META syntax” <../show_meta_syntax.md>`__ for its syntax details.
