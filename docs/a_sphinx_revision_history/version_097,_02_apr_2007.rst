Version 0.9.7, 02 apr 2007
--------------------------

-  added support for ``sql_str2ordinal_column``

-  added support for upto 5 sort-by attrs (in extended sorting mode)

-  added support for separate groups sorting clause (in group-by mode)

-  added support for on-the-fly attribute updates (PRE-ALPHA; will
   change heavily; use for preliminary testing ONLY)

-  added support for zero/NULL attributes

-  added support for 0.9.7 features to SphinxSE

-  added support for n-grams (alpha, 1-grams only for now)

-  added support for warnings reported to client

-  added support for exclude-filters

-  added support for prefix and infix indexing (see ``max_prefix_len``,
   ``max_infix_len``)

-  added ``@*`` syntax to reset current field to query language

-  added removal of duplicate entries in query index order

-  added PHP API workarounds for PHP signed/unsigned braindamage

-  added locks to avoid two concurrent indexers working on same index

-  added check for existing attributes vs. ``docinfo=none`` case

-  improved groupby code a lot (better precision, and upto 25x times
   faster in extreme cases)

-  improved error handling and reporting

-  improved handling of broken indexes (reports error instead of
   hanging/crashing)

-  improved ``mmap()`` limits for attributes and wordlists (now able to
   map over 4 GB on x64 and over 2 GB on x32 where possible)

-  improved ``malloc()`` pressure in head daemon (search time should not
   degrade with time any more)

-  improved ``test.php`` command line options

-  improved error reporting (distributed query, broken index etc issues
   now reported to client)

-  changed default network packet size to be 8M, added extra checks

-  fixed division by zero in BM25 on 1-document collections (in extended
   matching mode)

-  fixed ``.spl`` files getting unlinked

-  fixed crash in schema compatibility test

-  fixed UTF-8 Russian stemmer

-  fixed requested matches count when querying distributed agents

-  fixed signed vs. unsigned issues everywhere (ranged queries, CLI
   search output, and obtaining docid)

-  fixed potential crashes vs. negative query offsets

-  fixed 0-match docs vs. extended mode vs. stats

-  fixed group/timestamp filters being ignored if querying from older
   clients

-  fixed docs to mention ``pgsql`` source type

-  fixed issues with explicit ‘&’ in extended matching mode

-  fixed wrong assertion in SBCS encoder

-  fixed crashes with no-attribute indexes after rotate
