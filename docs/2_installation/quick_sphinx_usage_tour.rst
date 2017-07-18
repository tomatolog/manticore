Quick Sphinx usage tour
-----------------------

All the example commands below assume that you installed Sphinx in
``/usr/local/sphinx``, so ``searchd`` can be found in
``/usr/local/sphinx/bin/searchd``.

To use Sphinx, you will need to:

1. Create a configuration file.

   Default configuration file name is ``sphinx.conf``. All Sphinx
   programs look for this file in current working directory by default.

   Sample configuration file, ``sphinx.conf.dist``, which has all the
   options documented, is created by ``configure``. Copy and edit that
   sample file to make your own configuration: (assuming Sphinx is
   installed into ``/usr/local/sphinx/``)

   ::

       $ cd /usr/local/sphinx/etc
       $ cp sphinx.conf.dist sphinx.conf
       $ vi sphinx.conf

   Sample configuration file is setup to index ``documents`` table from
   MySQL database ``test``; so there's ``example.sql`` sample data file
   to populate that table with a few documents for testing purposes:

   ::

       $ mysql -u test < /usr/local/sphinx/etc/example.sql

2. Run the indexer to create full-text index from your data:

   ::

       $ cd /usr/local/sphinx/etc
       $ /usr/local/sphinx/bin/indexer --all

3. Query your newly created index!

Now query your indexes!

Connect to server:

::

    $ mysql -h0 -P9306

::

    SELECT * FROM test1 WHERE MATCH('my document');

::

    INSERT INTO rt VALUES (1, 'this is', 'a sample text', 11);

::

    INSERT INTO rt VALUES (2, 'some more', 'text here', 22);

::

    SELECT gid/11 FROM rt WHERE MATCH('text') GROUP BY gid;

::

    SELECT * FROM rt ORDER BY gid DESC;

::

    SHOW TABLES;

::

    SELECT *, WEIGHT() FROM test1 WHERE MATCH('"document one"/1');SHOW META;

::

    SET profiling=1;SELECT * FROM test1 WHERE id IN (1,2,4);SHOW PROFILE;

::

    SELECT id, id%3 idd FROM test1 WHERE MATCH('this is | nothing') GROUP BY idd;SHOW PROFILE;

::

    SELECT id FROM test1 WHERE MATCH('is this a good plan?');SHOW PLAN;

::

    SELECT COUNT(*) c, id%3 idd FROM test1 GROUP BY idd HAVING COUNT(*)>1;

::

    SELECT COUNT(*) FROM test1;

::

    CALL KEYWORDS ('one two three', 'test1');

::

    CALL KEYWORDS ('one two three', 'test1', 1);

Happy searching!
