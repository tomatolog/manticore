Version 2.0.7-release, 26 mar 2013
----------------------------------

Bug fixes
~~~~~~~~~

-  fixed #1475, memory leak in the expression parser

-  fixed #1457, error messages over 2KB were clipped

-  fixed #1454, searchd did not display an error message when the binlog
   path did not exist

-  fixed #1441, SHOW META in a query batch was returning the last
   non-batch error

-  fixed #1435, typo in the documentation

-  fixed #1430, rt\_flush\_period now works even with a disabled binlog

-  fixed #1427, overlong 4-byte UTF-8 codes in source text could cause
   indexer crashes or index corruption

-  fixed #1418, warnings from local index searches were lost with
   dist\_threads>0

-  fixed #1417, crash handler now works on searchd startup stage, too
   (eg. to report index load time crashes)

-  fixed #1410, bad numerics like ‘123abc’ now result in a proper
   SphinxQL error message

-  fixed #1404, a tiny memory leak in shared mutex

-  fixed #1394, race in –iostats caused incorrect I/O statistics in
   threaded modes

-  fixed #1391, QUORUM operator vs docinfo=inline returned wrong
   attribute values

-  fixed #1389, edge case in the ORDER operator caused occasionally
   searchd crashes

-  fixed #1382, query parts with field limits but without real keywords
   (like ‘@name {’) are now simply ignored and no longer cause a query
   syntax error

-  fixed #1370, Windows indexer builds failed to fetch rows from MSSQL
   2012

-  fixed #1368, ORDER BY RAND() did not work in RT indexes

-  fixed #1364, queries with hitless words could occasionally crash
   searchd

-  fixed #1363, '\*' in charset\_table was causing query syntax errors
   with enable\_star=1

-  fixed #1353, added filtering by ‘id’ syntax (in addition to ‘@id’) to
   ManticoreSE

-  fixed #1346, fixed NEAR operator behavior vs duplicated keywords

-  fixed #1345, invalid PROXIMITY operator threshold now causes a query
   syntax error rather than unexpected search behavior

-  fixed #1343, misconfigured indexes with 0 full text fields are now
   explicitly forbidden

-  fixed #1342, specific error messages (from the preload stage) went
   missing when failing to load the indexes

-  fixed #1339, no warning on inconsistent word statistics

-  fixed #1335, typo in searchd help screen

-  fixed #1334, typo in SELECT documentation

-  fixed #1316, PHRASE operator did not match in a rare self-repeating
   document/query case

-  fixed #1297, letting queries complete gracefully instead of killing
   them off in seamless\_rotate=1, workers=prefork case

-  fixed #1295, mentioned index naming requirements (proper identifier)
   in the FROM clause docs

-  fixed #1221, incorrect results when using @groupby in select list via
   SphinxAPI with compat\_sphinxql\_magics=0

-  fixed #1180, special SPZ chars occasionally leaking into snippets

-  fixed #1171, preforked children did not reload logs on SIGUSR1

-  fixed #1150, added support for ``id`` syntax in DELETE and parents in
   WHERE

-  fixed #1135, crashes when using MVA/strings attributes in expression
   ranker

-  fixed #1124, corrupted attributes after merging with an empty index

-  fixed #1090, ManticoreSE snippets UDF updated to support MySQL 5.5

-  fixed #1041, added initial support for MVA updates (and other mutex
   protected things) on FreeBSD

-  fixed #999, fullscan returned empty result sets in mixed batches of
   fullscan and fulltext queries

-  fixed #921, document count/bytes 32bit overflow in indexer progress
   output

-  fixed #539, added processing suffix rules with dots in .affix file to
   spelldump

-  fixed #481, rotation did not work on Windows with preopen=1

-  fixed #268, added warnings about duplicate elements in xmlpipe2

-  fixed CSphStaticMutex (double initialization issue)

-  fixed documentation typo in SQL data sources

-  fixed too-late initialization of mutex at daemon

-  fixed that an instance of searchd resurrected by watchdog could leak
   resources and/or crash

-  added a console message about crashes during index loading at startup

-  added more debug info about failed index loading
