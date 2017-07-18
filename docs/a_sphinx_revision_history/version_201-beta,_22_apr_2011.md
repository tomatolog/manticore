## Version 2.0.1-beta, 22 apr 2011 {#version-2-0-1-beta-22-apr-2011}

### New general features {#new-general-features}

*   added remapping support to [blend_chars](../index_configuration_options/blendchars.md) directive

*   added multi-threaded snippet batches support (requires a batch sent via API, [dist_threads](../searchd_program_configuration_options/distthreads.md), and `load_files`)

*   added collations ([collation_server](../searchd_program_configuration_options/collationserver.md), [collation_libc_locale directives](../searchd_program_configuration_options/collationlibc_locale.md))

*   added support for sorting and grouping on string attributes (`ORDER BY`, `GROUP BY`, `WITHIN GROUP ORDER BY`)

*   added UDF support ([plugin_dir](../common_section_configuration_options/plugindir.md) directive; [CREATE FUNCTION](../create_function_syntax.md), [DROP FUNCTION](../drop_function_syntax.md) statements)

*   added [query_log_format](../searchd_program_configuration_options/querylog_format.md) directive, [SET GLOBAL query_log_format | log_level = ...](../set_syntax.md) statements; and connection id tracking

*   added [sql_column_buffers](../data_source_configuration_options/sqlcolumn_buffers.md) directive, fixed out-of-buffer column handling in ODBC/MS SQL sources

*   added [blend_mode](../index_configuration_options/blendmode.md) directive that enables indexing multiple variants of a blended sequence

*   added UNIX socket support to C, Ruby APIs

*   added ranged query support to [sql_joined_field](../data_source_configuration_options/sqljoined_field.md)

*   added [rt_flush_period](../searchd_program_configuration_options/rtflush_period.md) directive

*   added [thread_stack](../searchd_program_configuration_options/threadstack.md) directive

*   added SENTENCE, PARAGRAPH, ZONE operators (and [index_sp](../index_configuration_options/indexsp.md), [index_zones](../index_configuration_options/indexzones.md) directives)

*   added keywords dictionary support (and [dict](../index_configuration_options/dict.md), [expansion_limit](../searchd_program_configuration_options/expansionlimit.md) directives)

*   added `passage_boundary`, `emit_zones` options to snippets

*   added [a watchdog process](../searchd_program_configuration_options/watchdog.md) in threaded mode

*   added persistent MVA updates

*   added crash dumps to `searchd.log`, deprecated `crash_log_path` directive

*   added id32 index support in id64 binaries (EXPERIMENTAL)

*   added SphinxSE support for DELETE and REPLACE on SphinxQL tables

### New SphinxQL features {#new-sphinxql-features}

*   added new, more SQL compliant SphinxQL syntax; and a compat_sphinxql_magics directive

*   added [CRC32()](../5_searching/expressions,_functions,_and_operators/miscellaneous_functions.md#expr-func-crc32), [DAY()](../5_searching/expressions,_functions,_and_operators/date_and_time_functions.md#expr-func-day), [MONTH()](../5_searching/expressions,_functions,_and_operators/date_and_time_functions.md#expr-func-month), [YEAR()](../5_searching/expressions,_functions,_and_operators/date_and_time_functions.md#expr-func-year), [YEARMONTH()](../5_searching/expressions,_functions,_and_operators/date_and_time_functions.md#expr-func-yearmonth), [YEARMONTHDAY()](../5_searching/expressions,_functions,_and_operators/date_and_time_functions.md#expr-func-yearmonthday) functions

*   added [DIV, MOD, and % operators](../5_searching/expressions,_functions,_and_operators/operators.md#expr-ari-ops)

*   added [reverse_scan=(0|1)](../select_syntax.md) option to SELECT

*   added support for MySQL packets over 16M

*   added dummy SHOW VARIABLES, SHOW COLLATION, and SET character_set_results support (to support handshake with certain client libraries and frameworks)

*   added [mysql_version_string](../searchd_program_configuration_options/mysqlversion_string.md) directive (to workaround picky MySQL client libraries)

*   added support for global filter variables, [SET GLOBAL @uservar=(int_list)](../set_syntax.md)

*   added [DELETE ... IN (id_list)](../delete_syntax.md) syntax support

*   added C-style comments syntax (for example, `SELECT /*!40000 some comment*/ id FROM test`)

*   added [UPDATE ... WHERE id=X](../update_syntax.md) syntax support

*   added [SphinxQL multi-query support](../multi-statement_queries.md)

*   added [DESCRIBE](../describe_syntax.md), [SHOW TABLES](../show_tables_syntax.md) statements

### New command-line switches {#new-command-line-switches}

*   added `--print-queries` switch to `indexer` that dumps SQL queries it runs

*   added `--sighup-each` switch to `indexer` that rotates indexes one by one

*   added `--strip-path` switch to `searchd` that skips file paths embedded in the index(-es)

*   added `--dumpconfig` switch to `indextool` that dumps an index header in `sphinx.conf` format

### Major changes and optimizations {#major-changes-and-optimizations}

*   changed default preopen_indexes value to 1

*   optimized English stemmer (results in 1.3x faster snippets and indexing with morphology=stem_en)

*   optimized snippets, 1.6x general speedup

*   optimized const-list parsing in SphinxQL

*   optimized full-document highlighting CPU/RAM use

*   optimized binlog replay (improved performance on K-list update)

### Bug fixes {#bug-fixes}

*   fixed #767, joined fields vs ODBC sources

*   fixed #757, wordforms shared by indexes with different settings

*   fixed #733, loading of indexes in formats prior to v.14

*   fixed #763, occasional snippets failures

*   fixed #648, occasionally missed rotations on multiple SIGHUPs

*   fixed #750, an RT segment merge leading to false positives and/or crashes in some cases

*   fixed #755, zones in snippets output

*   fixed #754, stopwords counting at snippet passage generation

*   fixed #723, fork/prefork index rotation in children processes

*   fixed #696, freeze on zero threshold in quorum operator

*   fixed #732, query escaping in SphinxSE

*   fixed #739, occasional crashes in MT mode on result set send

*   fixed #746, crash with a named list in SphinxQL option

*   fixed #674, AVG vs group order

*   fixed #734, occasional crashes attempting to report NULL errors

*   fixed #829, tail hits within field position modifier

*   fixed #712, missing query_mode, force_all_words snippet option defaults in Java API

*   fixed #721, added dupe removal on RT batch INSERT/REPLACE

*   fixed #720, potential extraneous highlighting after a blended keyword

*   fixed #702, exceptions vs star search

*   fixed #666, ext2 query grouping vs exceptions

*   fixed #688, WITHIN GROUP ORDER BY related crash

*   fixed #660, multi-queue batches vs dist_threads

*   fixed #678, crash on dict=keywords vs xmlpipe vs min_prefix_len

*   fixed #596, ECHILD vs scripted configs

*   fixed #653, dependency in expression, sorting, grouping

*   fixed #661, concurrent distributed searches vs workers=threads

*   fixed #646, crash on status query via UNIX socket

*   fixed #589, libexpat.dll missing from some Win32 build types

*   fixed #574, quorum match order

*   fixed multiple documentation issues (#372, #483, #495, #601, #623, #632, #654)

*   fixed that ondisk_dict did not affect RT indexes

*   fixed that string attributes check in indextool --check was erroneously sensitive to string data order

*   fixed a rare crash when using BEFORE operator

*   fixed an issue with multiforms vs BuildKeywords()

*   fixed an edge case in OR operator (emitted wrong hits order sometimes)

*   fixed aliasing in docinfo accessors that lead to very rare crashes and/or missing results

*   fixed a syntax error on a short token at the end of a query

*   fixed id64 filtering and performance degradation with range filters

*   fixed missing rankers in libsphinxclient

*   fixed missing SPH04 ranker in SphinxSE

*   fixed column names in sql_attr_multi sample (works with example.sql now)

*   fixed an issue with distributed local+remote setup vs aggregate functions

*   fixed case sensitive columns names in RT indexes

*   fixed a crash vs strings from multiple indexes in result set

*   fixed blended keywords vs snippets

*   fixed secure_connection vs MySQL protocol vs MySQL.NET connector

*   fixed that Python API did not works with Python 2.3

*   fixed overshort_step vs snippets

*   fixed keyword staistics vs dist_threads searching

*   fixed multiforms vs query parsing (vs quorum)

*   fixed missed quorum words vs RT segments

*   fixed blended keywords occasionally skipping extra character when querying (eg &quot;abc[]&quot;)

*   fixed Python API to handle int32 values

*   fixed prefix and infix indexing of joined fields

*   fixed MVA ranged query

*   fixed missing blended state reset on document boundary

*   fixed a crash on missing index while replaying binlog

*   fixed an error message on filter values overrun

*   fixed passage duplication in snippets in weight_order mode

*   fixed select clauses over 1K vs remote agents

*   fixed overshort accounting vs soft-whitespace tokens

*   fixed rotation vs workers=threads

*   fixed schema issues vs distributed indexes

*   fixed blended-escaped sequence parsing issue

*   fixed MySQL IN clause (values order etc)

*   fixed that post_index did not execute when 0 documents were succesfully indexed

*   fixed field position limit vs many hits

*   fixed that joined fields missed an end marker at field end

*   fixed that xxx_step settings were missing from .sph index header

*   fixed libsphinxclient missing request cleanup in sphinx_query() (eg after network errors)

*   fixed that index_weights were ignored when grouping

*   fixed multi wordforms vs blend_chars

*   fixed broken MVA output in SphinxQL

*   fixed a few RT leaks

*   fixed an issue with RT string storage going missing

*   fixed an issue with repeated queries vs dist_threads

*   fixed an issue with string attributes vs buffer overrun in SphinxQL

*   fixed unexpected character data warnings within ignored xmlpipe tags

*   fixed a crash in snippets with NEAR syntax query

*   fixed passage duplication in snippets

*   fixed libsphinxclient SIGPIPE handling

*   fixed libsphinxclient vs VS2003 compiler bug