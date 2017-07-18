## Version 0.9.9-rc1, 17 nov 2008 {#version-0-9-9-rc1-17-nov-2008}

*   added [min_stemming_len](../index_configuration_options/minstemming_len.md) directive

*   added [IsConnectError()](../general_api_functions/isconnecterror.md) API call (helps distingusih API vs remote errors)

*   added duplicate log messages filter to searchd

*   added --nodetach debugging switch to searchd

*   added blackhole agents support for debugging/testing ([agent_blackhole](../index_configuration_options/agentblackhole.md) directive)

*   added [max_filters](../searchd_program_configuration_options/maxfilters.md), [max_filter_values](../searchd_program_configuration_options/maxfilter_values.md) directives (were hardcoded before)

*   added int64 expression evaluation path, automatic inference, and BIGINT() enforcer function

*   added crash handler for debugging (`crash_log_path` directive)

*   added MS SQL (aka SQL Server) source support (Windows only, [mssql_winauth](../data_source_configuration_options/mssqlwinauth.md) and mssql_unicode directives)

*   added indexer-side column unpacking feature ([unpack_zlib](../data_source_configuration_options/unpackzlib.md), [unpack_mysqlcompress](../data_source_configuration_options/unpackmysqlcompress.md) directives)

*   added nested brackers and NOTs support to [query language](../extended_query_syntax.md), rewritten query parser

*   added persistent connections support ([Open()](../persistent_connections/open.md) and [Close()](../persistent_connections/close.md) API calls)

*   added [index_exact_words](../index_configuration_options/indexexact_words.md) feature, and exact form operator to query language (&quot;hello =world&quot;)

*   added status variables support to SphinxSE (SHOW STATUS LIKE &#039;sphinx_%&#039;)

*   added [max_packet_size](../searchd_program_configuration_options/maxpacket_size.md) directive (was hardcoded at 8M before)

*   added UNIX socket support, and multi-interface support ([listen](../searchd_program_configuration_options/listen.md) directive)

*   added star-syntax support to [BuildExcerpts()](../additional_functionality/buildexcerpts.md) API call

*   added inplace inversion of .spa and .spp ([inplace_enable](../index_configuration_options/inplaceenable.md) directive, 1.5-2x less disk space for indexing)

*   added builtin Czech stemmer (morphology=stem_cz)

*   added [IDIV(), NOW(), INTERVAL(), IN() functions](../5_searching/sorting_modes.md#sph-sort-expr-mode) to expressions

*   added index-level early-reject based on filters

*   added MVA updates feature ([mva_updates_pool](../searchd_program_configuration_options/mvaupdates_pool.md) directive)

*   added select-list feature with computed expressions support (see [SetSelect()](../general_query_settings/setselect.md) API call, test.php --select switch), protocol 1.22

*   added integer expressions support (2x faster than float)

*   added multiforms support (multiple source words in wordforms file)

*   added [legacy rankers](../full-text_search_query_settings/setrankingmode.md) (MATCH_ALL/MATCH_ANY/etc), removed legacy matching code (everything runs on V2 engine now)

*   added [field position limit](../extended_query_syntax.md) modifier to field operator (syntax: @title[50] hello world)

*   added killlist support ([sql_query_killlist](../data_source_configuration_options/sqlquery_killlist.md) directive, --merge-killlists switch)

*   added on-disk SPI support (ondisk_dict directive)

*   added indexer IO stats

*   added periodic .spa flush ([attr_flush_period](../searchd_program_configuration_options/attrflush_period.md) directive)

*   added config reload on SIGHUP

*   added per-query attribute overrides feature (see [SetOverride()](../general_query_settings/setoverride.md) API call); protocol 1.21

*   added signed 64bit attrs support ([sql_attr_bigint](../data_source_configuration_options/sqlattr_bigint.md) directive)

*   improved HTML stripper to also skip PIs (&lt;? ... ?&gt;, such as &lt;?php ... ?&gt;)

*   improved excerpts speed (upto 50x faster on big documents)

*   fixed a short window of searchd inaccessibility on startup (started listen()ing too early before)

*   fixed .spa loading on systems where read() is 2GB capped

*   fixed infixes vs morphology issues

*   fixed backslash escaping, added backslash to EscapeString()

*   fixed handling of over-2GB dictionary files (.spi)