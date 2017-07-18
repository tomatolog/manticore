## Version 0.9.8, 14 jul 2008 {#version-0-9-8-14-jul-2008}

### Indexing {#indexing}

*   added support for 64-bit document and keyword IDs, --enable-id64 switch to configure

*   added support for floating point attributes

*   added support for bitfields in attributes, [sql_attr_bool](../data_source_configuration_options/sqlattr_bool.md) directive and bit-widths part in [sql_attr_uint](../data_source_configuration_options/sqlattr_uint.md) directive

*   added support for multi-valued attributes (MVA)

*   added metaphone preprocessor

*   added libstemmer library support, provides stemmers for a number of additional languages

*   added xmlpipe2 source type, that supports arbitrary fields and attributes

*   added word form dictionaries, [wordforms](../index_configuration_options/wordforms.md) directive (and spelldump utility)

*   added tokenizing exceptions, [exceptions](../index_configuration_options/exceptions.md) directive

*   added an option to fully remove element contents to HTML stripper, [html_remove_elements](../index_configuration_options/htmlremove_elements.md) directive

*   added HTML entities decoder (with full XHTML1 set support) to HTML stripper

*   added per-index HTML stripping settings, [html_strip](../index_configuration_options/htmlstrip.md), [html_index_attrs](../index_configuration_options/htmlindex_attrs.md), and [html_remove_elements](../index_configuration_options/htmlremove_elements.md) directives

*   added IO load throttling, [max_iops](../indexer_program_configuration_options/maxiops.md) and [max_iosize](../indexer_program_configuration_options/maxiosize.md) directives

*   added SQL load throttling, [sql_ranged_throttle](../data_source_configuration_options/sqlranged_throttle.md) directive

*   added an option to index prefixes/infixes for given fields only, [prefix_fields](../index_configuration_options/prefixfields.md) and [infix_fields](../index_configuration_options/infixfields.md) directives

*   added an option to ignore certain characters (instead of just treating them as whitespace), [ignore_chars](../index_configuration_options/ignorechars.md) directive

*   added an option to increment word position on phrase boundary characters, [phrase_boundary](../index_configuration_options/phraseboundary.md) and [phrase_boundary_step](../index_configuration_options/phraseboundary_step.md) directives

*   added --merge-dst-range switch (and filters) to index merging feature (--merge switch)

*   added [mysql_connect_flags](../data_source_configuration_options/mysqlconnect_flags.md) directive (eg. to reduce indexing time MySQL network traffic and/or time)

*   improved ordinals sorting; now runs in fixed RAM

*   improved handling of documents with zero/NULL ids, now skipping them instead of aborting

### Search daemon {#search-daemon}

*   added an option to unlink old index on succesful rotation, [unlink_old](../searchd_program_configuration_options/unlinkold.md) directive

*   added an option to keep index files open at all times (fixes subtle races on rotation), [preopen](../index_configuration_options/preopen.md) and [preopen_indexes](../searchd_program_configuration_options/preopenindexes.md) directives

*   added an option to profile searchd disk I/O, --iostats command-line option

*   added an option to rotate index seamlessly (fully avoids query stalls), [seamless_rotate](../searchd_program_configuration_options/seamlessrotate.md) directive

*   added HTML stripping support to excerpts (uses per-index settings)

*   added &#039;exact_phrase&#039;, &#039;single_passage&#039;, &#039;use_boundaries&#039;, &#039;weight_order &#039;options to [BuildExcerpts()](../additional_functionality/buildexcerpts.md) API call

*   added distributed attribute updates propagation

*   added distributed retries on master node side

*   added log reopen on SIGUSR1

*   added --stop switch (sends SIGTERM to running instance)

*   added Windows service mode, and --servicename switch

*   added Windows --rotate support

*   improved log timestamping, now with millisecond precision

### Querying {#querying}

*   added extended engine V2 (faster, cleaner, better; SPH_MATCH_EXTENDED2 mode)

*   added ranking modes support (V2 engine only; [SetRankingMode()](../full-text_search_query_settings/setrankingmode.md) API call)

*   added quorum searching support to query language (V2 engine only; example: &quot;any three of all these words&quot;/3)

*   added query escaping support to query language, and [EscapeString()](../additional_functionality/escapestring.md) API call

*   added multi-field syntax support to query language (example: &quot;@(field1,field2) something&quot;), and @@relaxed field checks option

*   added optional star-syntax (&#039;word*&#039;) support in keywords, enable_star directive (for prefix/infix indexes only)

*   added full-scan support (query must be fully empty; can perform block-reject optimization)

*   added COUNT(DISTINCT(attr)) calculation support, [SetGroupDistinct()](../group_by_settings/setgroupdistinct.md) API call

*   added group-by on MVA support, [SetArrayResult()](../general_api_functions/setarrayresult.md) PHP API call

*   added per-index weights feature, [SetIndexWeights()](../full-text_search_query_settings/setindexweights.md) API call

*   added geodistance support, [SetGeoAnchor()](../result_set_filtering_settings/setgeoanchor.md) API call

*   added result set sorting by arbitrary expressions in run time (eg. &quot;@weight+log(price)*2.5&quot;), SPH_SORT_EXPR mode

*   added result set sorting by @custom compile-time sorting function (see src/sphinxcustomsort.inl)

*   added result set sorting by @random value

*   added result set merging for indexes with different schemas

*   added query comments support (3rd arg to [Query()](../querying/query.md)/[AddQuery()](../querying/addquery.md) API calls, copied verbatim to query log)

*   added keyword extraction support, [BuildKeywords()](../additional_functionality/buildkeywords.md) API call

*   added binding field weights by name, [SetFieldWeights()](../full-text_search_query_settings/setfieldweights.md) API call

*   added optional limit on query time, [SetMaxQueryTime()](../general_query_settings/setmaxquerytime.md) API call

*   added optional limit on found matches count (4rd arg to [SetLimits()](../general_query_settings/setlimits.md) API call, so-called &#039;cutoff&#039;)

### APIs and SphinxSE {#apis-and-sphinxse}

*   added pure C API (libsphinxclient)

*   added Ruby API (thanks to Dmytro Shteflyuk)

*   added Java API

*   added SphinxSE support for MVAs (use varchar), floats (use float), 64bit docids (use bigint)

*   added SphinxSE options &quot;floatrange&quot;, &quot;geoanchor&quot;, &quot;fieldweights&quot;, &quot;indexweights&quot;, &quot;maxquerytime&quot;, &quot;comment&quot;, &quot;host&quot; and &quot;port&quot;; and support for &quot;expr:CLAUSE&quot;

*   improved SphinxSE max query size (using MySQL condition pushdown), upto 256K now

### General {#general}

*   added scripting (shebang syntax) support to config files (example: #!/usr/bin/php in the first line)

*   added unified config handling and validation to all programs

*   added unified documentation

*   added .spec file for RPM builds

*   added automated testing suite

*   improved index locking, now fcntl()-based instead of buggy file-existence-based

*   fixed unaligned RAM accesses, now works on SPARC and ARM

### Changes and fixes since 0.9.8-rc2 {#changes-and-fixes-since-0-9-8-rc2}

*   added pure C API (libsphinxclient)

*   added Ruby API

*   added SetConnectTimeout() PHP API call

*   added allowed type check to UpdateAttributes() handler (bug #174)

*   added defensive MVA checks on index preload (protection against broken indexes, bug #168)

*   added sphinx-min.conf sample file

*   added --without-iconv switch to configure

*   removed redundant -lz dependency in searchd

*   removed erroneous &quot;xmlpipe2 deprecated&quot; warning

*   fixed EINTR handling in piped read (bug #166)

*   fixup query time before logging and sending to client (bug #153)

*   fixed attribute updates vs full-scan early-reject index (bug #149)

*   fixed gcc warnings (bug #160)

*   fixed mysql connection attempt vs pgsql source type (bug #165)

*   fixed 32-bit wraparound when preloading over 2 GB files

*   fixed &quot;out of memory&quot; message vs over 2 GB allocs (bug #116)

*   fixed unaligned RAM access detection on ARM (where unaligned reads do not crash but produce wrong results)

*   fixed missing full scan results in some cases

*   fixed several bugs in --merge, --merge-dst-range

*   fixed @geodist vs MultiQuery and filters, @expr vs MultiQuery

*   fixed GetTokenEnd() vs 1-grams (was causing crash in excerpts)

*   fixed sql_query_range to handle empty strings in addition to NULL strings (Postgres specific)

*   fixed morphology=none vs infixes

*   fixed case sensitive attributes names in UpdateAttributes()

*   fixed ext2 ranking vs. stopwords (now using atompos from query parser)

*   fixed EscapeString() call

*   fixed escaped specials (now handled as whitespace if not in charset)

*   fixed schema minimizer (now handles type/size mismatches)

*   fixed word stats in extended2; stemmed form is now returned

*   fixed spelldump case folding vs dictionary-defined character sets

*   fixed Postgres BOOLEAN handling

*   fixed enforced &quot;inline&quot; docinfo on empty indexes (normally ok, but index merge was really confused)

*   fixed rare count(distinct) out-of-bounds issue (it occasionaly caused too high @distinct values)

*   fixed hangups on documents with id=DOCID_MAX in some cases

*   fixed rare crash in tokenizer (prefixed synonym vs. input stream eof)

*   fixed query parser vs &quot;aaa (bbb ccc)|ddd&quot; queries

*   fixed BuildExcerpts() request in Java API

*   fixed Postgres specific memory leak

*   fixed handling of overshort keywords (less than min_word_len)

*   fixed HTML stripper (now emits space after indexed attributes)

*   fixed 32-field case in query parser

*   fixed rare count(distinct) vs. querying multiple local indexes vs. reusable sorter issue

*   fixed sorting of negative floats in SPH_SORT_EXTENDED mode