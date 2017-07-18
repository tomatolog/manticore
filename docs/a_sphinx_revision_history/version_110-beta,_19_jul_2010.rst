Version 1.10-beta, 19 jul 2010
------------------------------

-  added RT indexes support (`Chapter 4, *Real-time
   indexes* <../4_real-time_indexes/README.html>`__)

-  added prefork and threads support
   (`workers <../searchd_program_configuration_options/workers.html>`__
   directives)

-  added multi-threaded local searches in distributed indexes
   (`dist\_threads <../searchd_program_configuration_options/distthreads.html>`__
   directive)

-  added common subquery cache
   (`subtree\_docs\_cache <../searchd_program_configuration_options/subtreedocs_cache.html>`__,
   `subtree\_hits\_cache <../searchd_program_configuration_options/subtreehits_cache.html>`__
   directives)

-  added string attributes support
   (`sql\_attr\_string <../data_source_configuration_options/sqlattr_string.html>`__,
   `sql\_field\_string <../data_source_configuration_options/sqlfield_string.html>`__,
   `xml\_attr\_string <../data_source_configuration_options/xmlpipeattr_string.html>`__,
   `xml\_field\_string <../data_source_configuration_options/xmlpipefield_string.html>`__
   directives)

-  added indexing-time word counter (``sql_attr_str2wordcount``,
   ``sql_field_str2wordcount`` directives)

-  added `CALL SNIPPETS() <../call_snippets_syntax.html>`__, `CALL
   KEYWORDS() <../call_keywords_syntax.html>`__ SphinxQL statements

-  added ``field_weights``, ``index_weights`` options to SphinxQL
   `SELECT <../select_syntax.html>`__ statement

-  added insert-only SphinxQL-talking tables to SphinxSE
   (connection=‘sphinxql://host[:port]/index’)

-  added ``select`` option to SphinxSE queries

-  added backtrace on crash to ``searchd``

-  added SQL+FS indexing, aka loading files by names fetched from SQL
   (`sql\_file\_field <../data_source_configuration_options/sqlfile_field.html>`__
   directive)

-  added a watchdog in threads mode to ``searchd``

-  added automatic row phantoms elimination to index merge

-  added hitless indexing support (hitless\_words directive)

-  added –check, –strip-path, –htmlstrip, –dumphitlist … –wordid
   switches to `indextool <../indextool_command_reference.html>`__

-  added –stopwait, –logdebug switches to
   `searchd <../searchd_command_reference.html>`__

-  added –dump-rows, –verbose switches to
   `indexer <../indexer_command_reference.html>`__

-  added “blended” characters indexing support
   (`blend\_chars <../index_configuration_options/blendchars.html>`__
   directive)

-  added joined/payload field indexing
   (`sql\_joined\_field <../data_source_configuration_options/sqljoined_field.html>`__
   directive)

-  added `FlushAttributes() API
   call <../additional_functionality/flushattributes.html>`__

-  added query\_mode, force\_all\_words, limit\_passages, limit\_words,
   start\_passage\_id, load\_files, html\_strip\_mode, allow\_empty
   options, and %PASSAGE\_ID% macro in before\_match, after\_match
   options to
   `BuildExcerpts() <../additional_functionality/buildexcerpts.html>`__
   API call

-  added @groupby/@count/@distinct columns support to SELECT (but not to
   expressions)

-  added query-time keyword expansion support
   (`expand\_keywords <../index_configuration_options/expandkeywords.html>`__
   directive,
   `SPH\_RANK\_SPH04 <../full-text_search_query_settings/setrankingmode.html>`__
   ranker)

-  added query batch size limit option
   (`max\_batch\_queries <../searchd_program_configuration_options/maxbatch_queries.html>`__
   directive; was hardcoded)

-  added SINT() function to expressions

-  improved SphinxQL syntax error reporting

-  improved expression optimizer (better constant handling)

-  improved dash handling within keywords (no longer treated as an
   operator)

-  improved snippets (better passage selection/trimming, around option
   now a hard limit)

-  optimized index format that yields ~20-30% smaller indexes

-  optimized sorting code (indexing time 1-5% faster on average; 100x
   faster in w.html case)

-  optimized searchd startup time (moved .spa preindexing to indexer),
   added a progress bar

-  optimized queries against indexes with many attributes (eliminated
   redundant copying)

-  optimized 1-keyword queries (performace regression introduced in
   0.9.9)

-  optimized SphinxQL protocol overheads, and performance on bigger
   result sets

-  optimized unbuffered attributes writes on index merge

-  changed attribute handling, duplicate names are strictly forbidden
   now

-  fixed that SphinxQL sessions could stall shutdown

-  fixed consts with leading minus in SphinxQL

-  fixed AND/OR precedence in expressions

-  fixed #334, AVG() on integers was not computed in floats

-  fixed #371, attribute flush vs 2+ GB files

-  fixed #373, segfault on distributed queries vs certain libc versions

-  fixed #398, stopwords not stopped in prefix/infix indexes

-  fixed #404, erroneous MVA failures in indextool –check

-  fixed #408, segfault on certain query batches (regular scan, plus a
   scan with MVA groupby)

-  fixed #431, occasional shutdown hangs in preforked workers

-  fixed #436, trunk checkout builds vs Solaris sh

-  fixed #440, escaping vs parentheses declared as valid in
   charset\_table

-  fixed #442, occasional non-aligned free in MVA indexing

-  fixed #447, occasional crashes in MVA indexing

-  fixed #449, pconn busyloop on aborted clients on certain arches

-  fixed #465, build issue on Alpha

-  fixed #468, build issue in libsphinxclient

-  fixed #472, multiple stopword files failing to load

-  fixed #489, buffer overflow in query logging

-  fixed #493, Python API assertion after error returned from Query()

-  fixed #500, malformed MySQL packet when sending MVAs

-  fixed #504, SIGPIPE in libsphinxclient

-  fixed #506, better MySQL protocol commands support in SphinxQL (PING
   etc)

-  fixed #509, indexing ranged results from stored procedures
