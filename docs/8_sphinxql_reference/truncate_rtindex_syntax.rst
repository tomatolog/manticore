TRUNCATE RTINDEX syntax
-----------------------

::


    TRUNCATE RTINDEX rtindex

TRUNCATE RTINDEX statement, added in version 2.1.1-beta, clears the RT
index completely. It disposes the in-memory data, unlinks all the index
data files, and releases the associated binary logs.

::


    mysql> TRUNCATE RTINDEX rt;
    Query OK, 0 rows affected (0.05 sec)

You may want to use this if you are using RT indices as “delta index”
files; when you build the main index, you need to wipe the delta index,
and thus TRUNCATE RTINDEX. You also need to use this command before
attaching an index; see `the section called “ATTACH INDEX
syntax” <../attach_index_syntax.html>`__.
