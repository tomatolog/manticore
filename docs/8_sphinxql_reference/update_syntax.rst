UPDATE syntax
-------------

::


    UPDATE index SET col1 = newval1 [, ...] WHERE where_condition [OPTION opt_name = opt_value [, ...]]

UPDATE statement was added in version 2.0.1-beta. Multiple attributes
and values can be specified in a single statement. Both RT and disk
indexes are supported.

As of version 2.0.2-beta, all attributes types (int, bigint, float,
MVA), except for strings and JSON attributes, can be dynamically
updated. Previously, some of these types were not supported.

``where_condition`` (also added in 2.0.2-beta) has the same syntax as in
the SELECT statement (see `the section called “SELECT
syntax” <../select_syntax.html>`__ for details).

When assigning the out-of-range values to 32-bit attributes, they will
be trimmed to their lower 32 bits without a prompt. For example, if you
try to update the 32-bit unsigned int with a value of 4294967297, the
value of 1 will actually be stored, because the lower 32 bits of
4294967297 (0x100000001 in hex) amount to 1 (0x00000001 in hex).

MVA values sets for updating (and also for INSERT or REPLACE, refer to
`the section called “INSERT and REPLACE
syntax” <../insert_and_replace_syntax.html>`__) must be specified as
comma-separated lists in parentheses. To erase the MVA value, just
assign () to it.

Starting from 2.2.1-beta version UPDATE can be used to update integer
and float values in JSON array. No strings, arrays and other types yet.

::


    mysql> UPDATE myindex SET enabled=0 WHERE id=123;
    Query OK, 1 rows affected (0.00 sec)

    mysql> UPDATE myindex
      SET bigattr=-100000000000,
        fattr=3465.23,
        mvattr1=(3,6,4),
        mvattr2=()
      WHERE MATCH('hehe') AND enabled=1;
    Query OK, 148 rows affected (0.01 sec)

OPTION clause. This is a Sphinx specific extension that lets you control
a number of per-update options. The syntax is:

::


    OPTION <optionname>=<value> [ , ... ]

The list of allowed options are the same as for
`SELECT <../select_syntax.html>`__ statement. Specifically for UPDATE
statement you can use these options:

-  ‘ignore\_nonexistent\_columns’ - this option, added in version
   2.1.1-beta, points that the update will silently ignore any warnings
   about trying to update a column which is not exists in current index
   schema.

   ‘strict’ - this option is used while updating JSON attributes. As of
   2.2.1-beta, it's possible to update just some types in JSON. And if
   you try to update, for example, array type you'll get error with
   ‘strict’ option on and warning otherwise.
