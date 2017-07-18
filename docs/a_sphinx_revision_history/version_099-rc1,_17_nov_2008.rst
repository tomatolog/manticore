Version 0.9.9-rc1, 17 nov 2008
------------------------------

-  added
   `min\_stemming\_len <../index_configuration_options/minstemming_len.md>`__
   directive

-  added
   `IsConnectError() <../general_api_functions/isconnecterror.md>`__ API
   call (helps distingusih API vs remote errors)

-  added duplicate log messages filter to searchd

-  added –nodetach debugging switch to searchd

-  added blackhole agents support for debugging/testing
   (`agent\_blackhole <../index_configuration_options/agentblackhole.md>`__
   directive)

-  added
   `max\_filters <../searchd_program_configuration_options/maxfilters.md>`__,
   `max\_filter\_values <../searchd_program_configuration_options/maxfilter_values.md>`__
   directives (were hardcoded before)

-  added int64 expression evaluation path, automatic inference, and
   BIGINT() enforcer function

-  added crash handler for debugging (``crash_log_path`` directive)

-  added MS SQL (aka SQL Server) source support (Windows only,
   `mssql\_winauth <../data_source_configuration_options/mssqlwinauth.md>`__
   and mssql\_unicode directives)

-  added indexer-side column unpacking feature
   (`unpack\_zlib <../data_source_configuration_options/unpackzlib.md>`__,
   `unpack\_mysqlcompress <../data_source_configuration_options/unpackmysqlcompress.md>`__
   directives)

-  added nested brackers and NOTs support to `query
   language <../extended_query_syntax.md>`__, rewritten query parser

-  added persistent connections support
   (`Open() <../persistent_connections/open.md>`__ and
   `Close() <../persistent_connections/close.md>`__ API calls)

-  added
   `index\_exact\_words <../index_configuration_options/indexexact_words.md>`__
   feature, and exact form operator to query language (“hello =world”)

-  added status variables support to SphinxSE (SHOW STATUS LIKE
   ‘sphinx\_%’)

-  added
   `max\_packet\_size <../searchd_program_configuration_options/maxpacket_size.md>`__
   directive (was hardcoded at 8M before)

-  added UNIX socket support, and multi-interface support
   (`listen <../searchd_program_configuration_options/listen.md>`__
   directive)

-  added star-syntax support to
   `BuildExcerpts() <../additional_functionality/buildexcerpts.md>`__
   API call

-  added inplace inversion of .spa and .spp
   (`inplace\_enable <../index_configuration_options/inplaceenable.md>`__
   directive, 1.5-2x less disk space for indexing)

-  added builtin Czech stemmer (morphology=stem\_cz)

-  added `IDIV(), NOW(), INTERVAL(), IN()
   functions <../5_searching/sorting_modes.md#sph-sort-expr-mode>`__ to
   expressions

-  added index-level early-reject based on filters

-  added MVA updates feature
   (`mva\_updates\_pool <../searchd_program_configuration_options/mvaupdates_pool.md>`__
   directive)

-  added select-list feature with computed expressions support (see
   `SetSelect() <../general_query_settings/setselect.md>`__ API call,
   test.php –select switch), protocol 1.22

-  added integer expressions support (2x faster than float)

-  added multiforms support (multiple source words in wordforms file)

-  added `legacy
   rankers <../full-text_search_query_settings/setrankingmode.md>`__
   (MATCH\_ALL/MATCH\_ANY/etc), removed legacy matching code (everything
   runs on V2 engine now)

-  added `field position limit <../extended_query_syntax.md>`__ modifier
   to field operator (syntax: @title [50] hello world)

-  added killlist support
   (`sql\_query\_killlist <../data_source_configuration_options/sqlquery_killlist.md>`__
   directive, –merge-killlists switch)

-  added on-disk SPI support (ondisk\_dict directive)

-  added indexer IO stats

-  added periodic .spa flush
   (`attr\_flush\_period <../searchd_program_configuration_options/attrflush_period.md>`__
   directive)

-  added config reload on SIGHUP

-  added per-query attribute overrides feature (see
   `SetOverride() <../general_query_settings/setoverride.md>`__ API
   call); protocol 1.21

-  added signed 64bit attrs support
   (`sql\_attr\_bigint <../data_source_configuration_options/sqlattr_bigint.md>`__
   directive)

-  improved HTML stripper to also skip PIs (<? … ?>, such as <?php … ?>)

-  improved excerpts speed (upto 50x faster on big documents)

-  fixed a short window of searchd inaccessibility on startup (started
   listen()ing too early before)

-  fixed .spa loading on systems where read() is 2GB capped

-  fixed infixes vs morphology issues

-  fixed backslash escaping, added backslash to EscapeString()

-  fixed handling of over-2GB dictionary files (.spi)
