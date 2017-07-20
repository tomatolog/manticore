Version 0.9.9-rc2, 08 apr 2009
------------------------------

-  added IsConnectError(), Open(), Close() calls to Java API (bug #240)

-  added
   `read\_buffer <../searchd_program_configuration_options/readbuffer.md>`__,
   `read\_unhinted <../searchd_program_configuration_options/readunhinted.md>`__
   directives

-  added checks for build options returned by mysql\_config (builds on
   Solaris now)

-  added fixed-RAM index merge (bug #169)

-  added logging chained queries count in case of (optimized)
   multi-queries

-  added
   `GEODIST() <../5_searching/sorting_modes.md#sph-sort-expr-mode>`__
   function

-  added `–status switch to searchd <../searchd_command_reference.md>`__

-  added MySpell (OpenOffice) affix file support (bug #281)

-  added `ODBC
   support <../data_source_configuration_options/odbcdsn.md>`__ (both
   Windows and UnixODBC)

-  added support for @id in IN() (bug #292)

-  added support for `aggregate
   functions <../general_query_settings/setselect.md>`__ in GROUP BY
   (namely AVG, MAX, MIN, SUM)

-  added `MySQL UDF that builds
   snippets <../building_snippets_excerpts_via_mysql.md>`__ using
   searchd

-  added
   `write\_buffer <../indexer_program_configuration_options/writebuffer.md>`__
   directive (defaults to 1M)

-  added
   `xmlpipe\_fixup\_utf8 <../data_source_configuration_options/xmlpipefixup_utf8.md>`__
   directive

-  added suggestions sample

-  added microsecond precision int64 timer (bug #282)

-  added `listen\_backlog
   directive <../searchd_program_configuration_options/listenbacklog.md>`__

-  added
   `max\_xmlpipe2\_field <../indexer_program_configuration_options/maxxmlpipe2_field.md>`__
   directive

-  added `initial SphinxQL
   support <../mysql_protocol_support_and_sphinxql.md>`__ to mysql41
   handler, SELECT …/SHOW WARNINGS/STATUS/META are handled

-  added support for different network protocols, and mysql41 protocol

-  added `fieldmask
   ranker <../full-text_search_query_settings/setrankingmode.md>`__,
   updated ManticoreSE list of rankers

-  added
   `mysql\_ssl\_xxx <../data_source_configuration_options/mysqlssl_cert_,_mysqlssl_key_,_mysqlssl_ca.md>`__
   directives

-  added `–cpustats (requires clock\_gettime()) and –status
   switches <../searchd_command_reference.md>`__ to searchd

-  added performance counters,
   `Status() <../additional_functionality/status.md>`__ API call

-  added
   `overshort\_step <../index_configuration_options/overshortstep.md>`__
   and
   `stopword\_step <../index_configuration_options/stopwordstep.md>`__
   directives

-  added `strict order operator <../extended_query_syntax.md>`__ (aka
   operator before, eg. “one << two << three”)

-  added `indextool <../indextool_command_reference.md>`__ utility,
   moved –dumpheader there, added –debugdocids, –dumphitlist options

-  added own RNG, reseeded on @random sort query (bug #183)

-  added `field-start and field-end modifiers
   support <../extended_query_syntax.md>`__ (syntax is “^hello world$”;
   field-end requires reindex)

-  added MVA attribute support to IN() function

-  added `AND, OR, and NOT
   support <../5_searching/sorting_modes.md#sph-sort-expr-mode>`__ to
   expressions

-  improved logging of (optimized) multi-queries (now logging chained
   query count)

-  improved handshake error handling, fixed protocol version byte order
   (omg)

-  updated ManticoreSE to protocol 1.22

-  allowed phrase\_boundary\_step=-1 (trick to emulate keyword
   expansion)

-  removed SPH\_MAX\_QUERY\_WORDS limit

-  fixed CLI search vs documents missing from DB (bug #257)

-  fixed libsphinxclient results leak on subsequent sphinx\_run\_queries
   call (bug #256)

-  fixed libsphinxclient handling of zero max\_matches and cutoff (bug
   #208)

-  fixed Java API over-64K string reads (eg. big snippets) in Java API
   (bug #181)

-  fixed Java API 2nd Query() after network error in 1st Query() call
   (bug #308)

-  fixed typo-class bugs in SetFilterFloatRange (bug #259), SetSortMode
   (bug #248)

-  fixed missing @@relaxed support (bug #276), fixed missing error on
   @nosuchfield queries, documented @@relaxed

-  fixed UNIX socket permissions to 0777 (bug #288)

-  fixed xmlpipe2 crash on schemas with no fields, added better document
   structure checks

-  fixed (and optimized) expr parser vs IN() with huge (10K+) args count

-  fixed double EarlyCalc() in fullscan mode (minor performance impact)

-  fixed phrase boundary handling in some cases (on buffer end, on
   trailing whitespace)

-  fixes in snippets (aka excerpts) generation

-  fixed inline attrs vs id64 index corruption

-  fixed head searchd crash on config re-parse failure

-  fixed handling of numeric keywords with leading zeroes such as “007”
   (bug #251)

-  fixed junk in ManticoreSE status variables (bug #304)

-  fixed wordlist checkpoints serialization (bug #236)

-  fixed unaligned docinfo id access (bug #230)

-  fixed GetRawBytes() vs oversized blocks (headers with over 32K
   charset\_table should now work, bug #300)

-  fixed buffer overflow caused by too long dest wordform, updated tests

-  fixed IF() return type (was always int, is deduced now)

-  fixed legacy queries vs. special chars vs. multiple indexes

-  fixed write-write-read socket access pattern vs Nagle vs delays vs
   FreeBSD (oh wow)

-  fixed exceptions vs query-parser issue

-  fixed late calc vs @weight in expressions (bug #285)

-  fixed early lookup/calc vs filters (bug #284)

-  fixed emulated MATCH\_ANY queries (empty proximity and phrase queries
   are allowed now)

-  fixed MATCH\_ANY ranker vs fields with no matches

-  fixed index file size vs inplace\_enable (bug #245)

-  fixed that old logs were not closed on USR1 (bug #221)

-  fixed handling of ‘!’ alias to NOT operator (bug #237)

-  fixed error handling vs query steps (step failure was not reported)

-  fixed querying vs inline attributes

-  fixed stupid bug in escaping code, fixed EscapeString() and made it
   static

-  fixed parser vs @field -keyword, foo\|@field bar, “” queries (bug
   #310)
