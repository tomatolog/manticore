Version 2.0.1-beta, 22 apr 2011
-------------------------------

New general features
~~~~~~~~~~~~~~~~~~~~

-  added remapping support to
   `blend\_chars <../index_configuration_options/blendchars.md>`__
   directive

-  added multi-threaded snippet batches support (requires a batch sent
   via API,
   `dist\_threads <../searchd_program_configuration_options/distthreads.md>`__,
   and ``load_files``)

-  added collations
   (`collation\_server <../searchd_program_configuration_options/collationserver.md>`__,
   `collation\_libc\_locale
   directives <../searchd_program_configuration_options/collationlibc_locale.md>`__)

-  added support for sorting and grouping on string attributes
   (``ORDER BY``, ``GROUP BY``, ``WITHIN GROUP ORDER BY``)

-  added UDF support
   (`plugin\_dir <../common_section_configuration_options/plugindir.md>`__
   directive; `CREATE FUNCTION <../create_function_syntax.md>`__, `DROP
   FUNCTION <../drop_function_syntax.md>`__ statements)

-  added
   `query\_log\_format <../searchd_program_configuration_options/querylog_format.md>`__
   directive, `SET GLOBAL query\_log\_format \| log\_level =
   … <../set_syntax.md>`__ statements; and connection id tracking

-  added
   `sql\_column\_buffers <../data_source_configuration_options/sqlcolumn_buffers.md>`__
   directive, fixed out-of-buffer column handling in ODBC/MS SQL sources

-  added `blend\_mode <../index_configuration_options/blendmode.md>`__
   directive that enables indexing multiple variants of a blended
   sequence

-  added UNIX socket support to C, Ruby APIs

-  added ranged query support to
   `sql\_joined\_field <../data_source_configuration_options/sqljoined_field.md>`__

-  added
   `rt\_flush\_period <../searchd_program_configuration_options/rtflush_period.md>`__
   directive

-  added
   `thread\_stack <../searchd_program_configuration_options/threadstack.md>`__
   directive

-  added SENTENCE, PARAGRAPH, ZONE operators (and
   `index\_sp <../index_configuration_options/indexsp.md>`__,
   `index\_zones <../index_configuration_options/indexzones.md>`__
   directives)

-  added keywords dictionary support (and
   `dict <../index_configuration_options/dict.md>`__,
   `expansion\_limit <../searchd_program_configuration_options/expansionlimit.md>`__
   directives)

-  added ``passage_boundary``, ``emit_zones`` options to snippets

-  added `a watchdog
   process <../searchd_program_configuration_options/watchdog.md>`__ in
   threaded mode

-  added persistent MVA updates

-  added crash dumps to ``searchd.log``, deprecated ``crash_log_path``
   directive

-  added id32 index support in id64 binaries (EXPERIMENTAL)

-  added ManticoreSE support for DELETE and REPLACE on SphinxQL tables

New SphinxQL features
~~~~~~~~~~~~~~~~~~~~~

-  added new, more SQL compliant SphinxQL syntax; and a
   compat\_sphinxql\_magics directive

-  added
   `CRC32() <../5_searching/expressions,_functions,_and_operators/miscellaneous_functions.md#expr-func-crc32>`__,
   `DAY() <../5_searching/expressions,_functions,_and_operators/date_and_time_functions.md#expr-func-day>`__,
   `MONTH() <../5_searching/expressions,_functions,_and_operators/date_and_time_functions.md#expr-func-month>`__,
   `YEAR() <../5_searching/expressions,_functions,_and_operators/date_and_time_functions.md#expr-func-year>`__,
   `YEARMONTH() <../5_searching/expressions,_functions,_and_operators/date_and_time_functions.md#expr-func-yearmonth>`__,
   `YEARMONTHDAY() <../5_searching/expressions,_functions,_and_operators/date_and_time_functions.md#expr-func-yearmonthday>`__
   functions

-  added `DIV, MOD, and %
   operators <../5_searching/expressions,_functions,_and_operators/operators.md#expr-ari-ops>`__

-  added `reverse\_scan=(0\|1) <../select_syntax.md>`__ option to SELECT

-  added support for MySQL packets over 16M

-  added dummy SHOW VARIABLES, SHOW COLLATION, and SET
   character\_set\_results support (to support handshake with certain
   client libraries and frameworks)

-  added
   `mysql\_version\_string <../searchd_program_configuration_options/mysqlversion_string.md>`__
   directive (to workaround picky MySQL client libraries)

-  added support for global filter variables, [SET GLOBAL
   @uservar=(int\_list)](../set\_syntax.md)

-  added `DELETE … IN (id\_list) <../delete_syntax.md>`__ syntax support

-  added C-style comments syntax (for example,
   ``SELECT /*!40000 some comment*/ id FROM test``)

-  added `UPDATE … WHERE id=X <../update_syntax.md>`__ syntax support

-  added `SphinxQL multi-query
   support <../multi-statement_queries.md>`__

-  added `DESCRIBE <../describe_syntax.md>`__, `SHOW
   TABLES <../show_tables_syntax.md>`__ statements

New command-line switches
~~~~~~~~~~~~~~~~~~~~~~~~~

-  added ``--print-queries`` switch to ``indexer`` that dumps SQL
   queries it runs

-  added ``--sighup-each`` switch to ``indexer`` that rotates indexes
   one by one

-  added ``--strip-path`` switch to ``searchd`` that skips file paths
   embedded in the index(-es)

-  added ``--dumpconfig`` switch to ``indextool`` that dumps an index
   header in ``sphinx.conf`` format

Major changes and optimizations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  changed default preopen\_indexes value to 1

-  optimized English stemmer (results in 1.3x faster snippets and
   indexing with morphology=stem\_en)

-  optimized snippets, 1.6x general speedup

-  optimized const-list parsing in SphinxQL

-  optimized full-document highlighting CPU/RAM use

-  optimized binlog replay (improved performance on K-list update)

Bug fixes
~~~~~~~~~

-  fixed #767, joined fields vs ODBC sources

-  fixed #757, wordforms shared by indexes with different settings

-  fixed #733, loading of indexes in formats prior to v.14

-  fixed #763, occasional snippets failures

-  fixed #648, occasionally missed rotations on multiple SIGHUPs

-  fixed #750, an RT segment merge leading to false positives and/or
   crashes in some cases

-  fixed #755, zones in snippets output

-  fixed #754, stopwords counting at snippet passage generation

-  fixed #723, fork/prefork index rotation in children processes

-  fixed #696, freeze on zero threshold in quorum operator

-  fixed #732, query escaping in ManticoreSE

-  fixed #739, occasional crashes in MT mode on result set send

-  fixed #746, crash with a named list in SphinxQL option

-  fixed #674, AVG vs group order

-  fixed #734, occasional crashes attempting to report NULL errors

-  fixed #829, tail hits within field position modifier

-  fixed #712, missing query\_mode, force\_all\_words snippet option
   defaults in Java API

-  fixed #721, added dupe removal on RT batch INSERT/REPLACE

-  fixed #720, potential extraneous highlighting after a blended keyword

-  fixed #702, exceptions vs star search

-  fixed #666, ext2 query grouping vs exceptions

-  fixed #688, WITHIN GROUP ORDER BY related crash

-  fixed #660, multi-queue batches vs dist\_threads

-  fixed #678, crash on dict=keywords vs xmlpipe vs min\_prefix\_len

-  fixed #596, ECHILD vs scripted configs

-  fixed #653, dependency in expression, sorting, grouping

-  fixed #661, concurrent distributed searches vs workers=threads

-  fixed #646, crash on status query via UNIX socket

-  fixed #589, libexpat.dll missing from some Win32 build types

-  fixed #574, quorum match order

-  fixed multiple documentation issues (#372, #483, #495, #601, #623,
   #632, #654)

-  fixed that ondisk\_dict did not affect RT indexes

-  fixed that string attributes check in indextool –check was
   erroneously sensitive to string data order

-  fixed a rare crash when using BEFORE operator

-  fixed an issue with multiforms vs BuildKeywords()

-  fixed an edge case in OR operator (emitted wrong hits order
   sometimes)

-  fixed aliasing in docinfo accessors that lead to very rare crashes
   and/or missing results

-  fixed a syntax error on a short token at the end of a query

-  fixed id64 filtering and performance degradation with range filters

-  fixed missing rankers in libsphinxclient

-  fixed missing SPH04 ranker in ManticoreSE

-  fixed column names in sql\_attr\_multi sample (works with example.sql
   now)

-  fixed an issue with distributed local+remote setup vs aggregate
   functions

-  fixed case sensitive columns names in RT indexes

-  fixed a crash vs strings from multiple indexes in result set

-  fixed blended keywords vs snippets

-  fixed secure\_connection vs MySQL protocol vs MySQL.NET connector

-  fixed that Python API did not works with Python 2.3

-  fixed overshort\_step vs snippets

-  fixed keyword staistics vs dist\_threads searching

-  fixed multiforms vs query parsing (vs quorum)

-  fixed missed quorum words vs RT segments

-  fixed blended keywords occasionally skipping extra character when
   querying (eg “abc[]”)

-  fixed Python API to handle int32 values

-  fixed prefix and infix indexing of joined fields

-  fixed MVA ranged query

-  fixed missing blended state reset on document boundary

-  fixed a crash on missing index while replaying binlog

-  fixed an error message on filter values overrun

-  fixed passage duplication in snippets in weight\_order mode

-  fixed select clauses over 1K vs remote agents

-  fixed overshort accounting vs soft-whitespace tokens

-  fixed rotation vs workers=threads

-  fixed schema issues vs distributed indexes

-  fixed blended-escaped sequence parsing issue

-  fixed MySQL IN clause (values order etc)

-  fixed that post\_index did not execute when 0 documents were
   succesfully indexed

-  fixed field position limit vs many hits

-  fixed that joined fields missed an end marker at field end

-  fixed that xxx\_step settings were missing from .sph index header

-  fixed libsphinxclient missing request cleanup in sphinx\_query() (eg
   after network errors)

-  fixed that index\_weights were ignored when grouping

-  fixed multi wordforms vs blend\_chars

-  fixed broken MVA output in SphinxQL

-  fixed a few RT leaks

-  fixed an issue with RT string storage going missing

-  fixed an issue with repeated queries vs dist\_threads

-  fixed an issue with string attributes vs buffer overrun in SphinxQL

-  fixed unexpected character data warnings within ignored xmlpipe tags

-  fixed a crash in snippets with NEAR syntax query

-  fixed passage duplication in snippets

-  fixed libsphinxclient SIGPIPE handling

-  fixed libsphinxclient vs VS2003 compiler bug
