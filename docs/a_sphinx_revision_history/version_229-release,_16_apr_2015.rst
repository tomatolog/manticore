Version 2.2.9-release, 16 apr 2015
----------------------------------

Bug fixes
~~~~~~~~~

-  fixed #2228, removed ``searchd`` shutdown behavior on failed
   connection

-  fixed #2208, `ZONESPANLIST() <../extended_query_syntax.html>`__ support
   for RT indexes

-  fixed #2203, legacy API `SELECT <../9_api_reference/README.html>`__
   list

-  fixed #2201, ``indextool`` false positive error on RT index

-  fixed #2201, crash with string comparison at expressions and
   expression ranker

-  fixed #2199, invalid packedfactors JSON output for index with
   stopwords

-  fixed #2197, `TRUNCATE <../truncate_rtindex_syntax.html>`__ fails to
   remove disk chunk files after calling
   `OPTIMIZE <../optimize_index_syntax.html>`__

-  fixed #2196, .NET connector issue (UTC\_TIMESTAMP() support)

-  fixed #2190, incorrect `GROUP BY <../group_by_settings/README.html>`__
   outer JSON object

-  fixed #2176, agent used ``ha_strategy=random`` instead of specified
   in config

-  fixed #2144, query parser crash vs multiforms with heading numbers

-  fixed #2122, id64 daemon failed to load RT disk chunk with kill-list
   from id32 build

-  fixed #2120, aliased JSON elements support

-  fixed #1979, snippets generation and span length and lcs calculation
   in proximity queries

-  fixed truncated results (and a potential crash) vs long enough
   ZONESPANLIST() result
