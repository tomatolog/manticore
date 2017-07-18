.. raw:: html

   <div class="navheader">

A.36. Version 0.9.9-rc2, 08 apr 2009
`Prev <rel099.html>`__ 
Appendix A. Sphinx revision history
 `Next <rel099rc1.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect1">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: A.36. Version 0.9.9-rc2, 08 apr 2009
   :name: a.36.version-0.9.9-rc2-08-apr-2009
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="itemizedlist">

-  added IsConnectError(), Open(), Close() calls to Java API (bug
   `#240 <http://sphinxsearch.com/bugs/view.php?id=240>`__)

-  added `read\_buffer <conf-read-buffer.html>`__,
   `read\_unhinted <conf-read-unhinted.html>`__ directives

-  added checks for build options returned by mysql\_config (builds on
   Solaris now)

-  added fixed-RAM index merge (bug
   `#169 <http://sphinxsearch.com/bugs/view.php?id=169>`__)

-  added logging chained queries count in case of (optimized)
   multi-queries

-  added `GEODIST() <sorting-modes.html#sort-expr>`__ function

-  added `–status switch to searchd <ref-searchd.html>`__

-  added MySpell (OpenOffice) affix file support (bug
   `#281 <http://sphinxsearch.com/bugs/view.php?id=281>`__)

-  added `ODBC support <conf-odbc-dsn.html>`__ (both Windows and
   UnixODBC)

-  added support for @id in IN() (bug
   `#292 <http://sphinxsearch.com/bugs/view.php?id=292>`__)

-  added support for `aggregate functions <api-func-setselect.html>`__
   in GROUP BY (namely AVG, MAX, MIN, SUM)

-  added `MySQL UDF that builds snippets <sphinxse-snippets.html>`__
   using searchd

-  added `write\_buffer <conf-write-buffer.html>`__ directive (defaults
   to 1M)

-  added `xmlpipe\_fixup\_utf8 <conf-xmlpipe-fixup-utf8.html>`__
   directive

-  added suggestions sample

-  added microsecond precision int64 timer (bug
   `#282 <http://sphinxsearch.com/bugs/view.php?id=282>`__)

-  added `listen\_backlog directive <conf-listen-backlog.html>`__

-  added `max\_xmlpipe2\_field <conf-max-xmlpipe2-field.html>`__
   directive

-  added `initial SphinxQL support <sphinxql.html>`__ to mysql41
   handler, SELECT …/SHOW WARNINGS/STATUS/META are handled

-  added support for different network protocols, and mysql41 protocol

-  added `fieldmask ranker <api-func-setrankingmode.html>`__, updated
   SphinxSE list of rankers

-  added `mysql\_ssl\_xxx <conf-mysql-ssl.html>`__ directives

-  added `–cpustats (requires clock\_gettime()) and –status
   switches <ref-searchd.html>`__ to searchd

-  added performance counters, `Status() <api-func-status.html>`__ API
   call

-  added `overshort\_step <conf-overshort-step.html>`__ and
   `stopword\_step <conf-stopword-step.html>`__ directives

-  added `strict order operator <extended-syntax.html>`__ (aka operator
   before, eg. “one << two << three”)

-  added `indextool <ref-indextool.html>`__ utility, moved –dumpheader
   there, added –debugdocids, –dumphitlist options

-  added own RNG, reseeded on @random sort query (bug
   `#183 <http://sphinxsearch.com/bugs/view.php?id=183>`__)

-  added `field-start and field-end modifiers
   support <extended-syntax.html>`__ (syntax is “^hello world$”;
   field-end requires reindex)

-  added MVA attribute support to IN() function

-  added `AND, OR, and NOT support <sorting-modes.html#sort-expr>`__ to
   expressions

-  improved logging of (optimized) multi-queries (now logging chained
   query count)

-  improved handshake error handling, fixed protocol version byte order
   (omg)

-  updated SphinxSE to protocol 1.22

-  allowed phrase\_boundary\_step=-1 (trick to emulate keyword
   expansion)

-  removed SPH\_MAX\_QUERY\_WORDS limit

-  fixed CLI search vs documents missing from DB (bug
   `#257 <http://sphinxsearch.com/bugs/view.php?id=257>`__)

-  fixed libsphinxclient results leak on subsequent sphinx\_run\_queries
   call (bug `#256 <http://sphinxsearch.com/bugs/view.php?id=256>`__)

-  fixed libsphinxclient handling of zero max\_matches and cutoff (bug
   `#208 <http://sphinxsearch.com/bugs/view.php?id=208>`__)

-  fixed Java API over-64K string reads (eg. big snippets) in Java API
   (bug `#181 <http://sphinxsearch.com/bugs/view.php?id=181>`__)

-  fixed Java API 2nd Query() after network error in 1st Query() call
   (bug `#308 <http://sphinxsearch.com/bugs/view.php?id=308>`__)

-  fixed typo-class bugs in SetFilterFloatRange (bug
   `#259 <http://sphinxsearch.com/bugs/view.php?id=259>`__), SetSortMode
   (bug `#248 <http://sphinxsearch.com/bugs/view.php?id=248>`__)

-  fixed missing @@relaxed support (bug
   `#276 <http://sphinxsearch.com/bugs/view.php?id=276>`__), fixed
   missing error on @nosuchfield queries, documented @@relaxed

-  fixed UNIX socket permissions to 0777 (bug
   `#288 <http://sphinxsearch.com/bugs/view.php?id=288>`__)

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
   (bug `#251 <http://sphinxsearch.com/bugs/view.php?id=251>`__)

-  fixed junk in SphinxSE status variables (bug
   `#304 <http://sphinxsearch.com/bugs/view.php?id=304>`__)

-  fixed wordlist checkpoints serialization (bug
   `#236 <http://sphinxsearch.com/bugs/view.php?id=236>`__)

-  fixed unaligned docinfo id access (bug
   `#230 <http://sphinxsearch.com/bugs/view.php?id=230>`__)

-  fixed GetRawBytes() vs oversized blocks (headers with over 32K
   charset\_table should now work, bug
   `#300 <http://sphinxsearch.com/bugs/view.php?id=300>`__)

-  fixed buffer overflow caused by too long dest wordform, updated tests

-  fixed IF() return type (was always int, is deduced now)

-  fixed legacy queries vs. special chars vs. multiple indexes

-  fixed write-write-read socket access pattern vs Nagle vs delays vs
   FreeBSD (oh wow)

-  fixed exceptions vs query-parser issue

-  fixed late calc vs @weight in expressions (bug
   `#285 <http://sphinxsearch.com/bugs/view.php?id=285>`__)

-  fixed early lookup/calc vs filters (bug
   `#284 <http://sphinxsearch.com/bugs/view.php?id=284>`__)

-  fixed emulated MATCH\_ANY queries (empty proximity and phrase queries
   are allowed now)

-  fixed MATCH\_ANY ranker vs fields with no matches

-  fixed index file size vs inplace\_enable (bug
   `#245 <http://sphinxsearch.com/bugs/view.php?id=245>`__)

-  fixed that old logs were not closed on USR1 (bug
   `#221 <http://sphinxsearch.com/bugs/view.php?id=221>`__)

-  fixed handling of ‘!’ alias to NOT operator (bug
   `#237 <http://sphinxsearch.com/bugs/view.php?id=237>`__)

-  fixed error handling vs query steps (step failure was not reported)

-  fixed querying vs inline attributes

-  fixed stupid bug in escaping code, fixed EscapeString() and made it
   static

-  fixed parser vs @field -keyword, foo\|@field bar, “” queries (bug
   `#310 <http://sphinxsearch.com/bugs/view.php?id=310>`__)

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------------+---------------------------+-----------------------------------------+
| `Prev <rel099.html>`__                      | `Up <changelog.html>`__   |  `Next <rel099rc1.html>`__              |
+---------------------------------------------+---------------------------+-----------------------------------------+
| A.35. Version 0.9.9-release, 02 dec 2009    | `Home <index.html>`__     |  A.37. Version 0.9.9-rc1, 17 nov 2008   |
+---------------------------------------------+---------------------------+-----------------------------------------+

.. raw:: html

   </div>
