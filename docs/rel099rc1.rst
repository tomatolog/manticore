.. raw:: html

   <div class="navheader">

A.37. Version 0.9.9-rc1, 17 nov 2008
`Prev <rel099rc2.html>`__ 
Appendix A. Sphinx revision history
 `Next <rel0981.html>`__

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

.. rubric:: A.37. Version 0.9.9-rc1, 17 nov 2008
   :name: a.37.version-0.9.9-rc1-17-nov-2008
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="itemizedlist">

-  added `min\_stemming\_len <conf-min-stemming-len.html>`__ directive

-  added `IsConnectError() <api-func-isconnecterror.html>`__ API call
   (helps distingusih API vs remote errors)

-  added duplicate log messages filter to searchd

-  added –nodetach debugging switch to searchd

-  added blackhole agents support for debugging/testing
   (`agent\_blackhole <conf-agent-blackhole.html>`__ directive)

-  added `max\_filters <conf-max-filters.html>`__,
   `max\_filter\_values <conf-max-filter-values.html>`__ directives
   (were hardcoded before)

-  added int64 expression evaluation path, automatic inference, and
   BIGINT() enforcer function

-  added crash handler for debugging (``crash_log_path`` directive)

-  added MS SQL (aka SQL Server) source support (Windows only,
   `mssql\_winauth <conf-mssql-winauth.html>`__ and mssql\_unicode
   directives)

-  added indexer-side column unpacking feature
   (`unpack\_zlib <conf-unpack-zlib.html>`__,
   `unpack\_mysqlcompress <conf-unpack-mysqlcompress.html>`__
   directives)

-  added nested brackers and NOTs support to `query
   language <extended-syntax.html>`__, rewritten query parser

-  added persistent connections support (`Open() <api-func-open.html>`__
   and `Close() <api-func-close.html>`__ API calls)

-  added `index\_exact\_words <conf-index-exact-words.html>`__ feature,
   and exact form operator to query language (“hello =world”)

-  added status variables support to SphinxSE (SHOW STATUS LIKE
   ‘sphinx\_%’)

-  added `max\_packet\_size <conf-max-packet-size.html>`__ directive
   (was hardcoded at 8M before)

-  added UNIX socket support, and multi-interface support
   (`listen <conf-listen.html>`__ directive)

-  added star-syntax support to
   `BuildExcerpts() <api-func-buildexcerpts.html>`__ API call

-  added inplace inversion of .spa and .spp
   (`inplace\_enable <conf-inplace-enable.html>`__ directive, 1.5-2x
   less disk space for indexing)

-  added builtin Czech stemmer (morphology=stem\_cz)

-  added `IDIV(), NOW(), INTERVAL(), IN()
   functions <sorting-modes.html#sort-expr>`__ to expressions

-  added index-level early-reject based on filters

-  added MVA updates feature
   (`mva\_updates\_pool <conf-mva-updates-pool.html>`__ directive)

-  added select-list feature with computed expressions support (see
   `SetSelect() <api-func-setselect.html>`__ API call, test.php –select
   switch), protocol 1.22

-  added integer expressions support (2x faster than float)

-  added multiforms support (multiple source words in wordforms file)

-  added `legacy rankers <api-func-setrankingmode.html>`__
   (MATCH\_ALL/MATCH\_ANY/etc), removed legacy matching code (everything
   runs on V2 engine now)

-  added `field position limit <extended-syntax.html>`__ modifier to
   field operator (syntax: @title[50] hello world)

-  added killlist support
   (`sql\_query\_killlist <conf-sql-query-killlist.html>`__ directive,
   –merge-killlists switch)

-  added on-disk SPI support (ondisk\_dict directive)

-  added indexer IO stats

-  added periodic .spa flush
   (`attr\_flush\_period <conf-attr-flush-period.html>`__ directive)

-  added config reload on SIGHUP

-  added per-query attribute overrides feature (see
   `SetOverride() <api-func-setoverride.html>`__ API call); protocol
   1.21

-  added signed 64bit attrs support
   (`sql\_attr\_bigint <conf-sql-attr-bigint.html>`__ directive)

-  improved HTML stripper to also skip PIs (<? … ?>, such as <?php … ?>)

-  improved excerpts speed (upto 50x faster on big documents)

-  fixed a short window of searchd inaccessibility on startup (started
   listen()ing too early before)

-  fixed .spa loading on systems where read() is 2GB capped

-  fixed infixes vs morphology issues

-  fixed backslash escaping, added backslash to EscapeString()

-  fixed handling of over-2GB dictionary files (.spi)

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+---------------------------+---------------------------------------+
| `Prev <rel099rc2.html>`__               | `Up <changelog.html>`__   |  `Next <rel0981.html>`__              |
+-----------------------------------------+---------------------------+---------------------------------------+
| A.36. Version 0.9.9-rc2, 08 apr 2009    | `Home <index.html>`__     |  A.38. Version 0.9.8.1, 30 oct 2008   |
+-----------------------------------------+---------------------------+---------------------------------------+

.. raw:: html

   </div>
