Version 2.0.5-release, 28 jul 2012
----------------------------------

Bug fixes
~~~~~~~~~

-  fixed #1258, ``xmlpipe2`` refused to index indexes with
   ``docinfo=inline``

-  fixed #1257, legacy groupby modes vs ``dist_threads`` could
   occasionally return wrong search results (race condition)

-  fixed #1253, missing single-word query performance optimization
   (simplified ranker) vs prefix-expanded keywords vs ``dict=keywords``

-  fixed #1252, COUNT(\*) vs
   `dist\_threads <../searchd_program_configuration_options/distthreads.html>`__
   could occasionally crash (race condition)

-  fixed #1251, missing expression support in the
   `IN() <../5_searching/expressions,_functions,_and_operators/comparison_functions.html#expr-func-in>`__
   function

-  fixed #1245,
   `FlushAttributes <../additional_functionality/flushattributes.html>`__
   mistakenly disabled by
   `attr\_flush\_period=0 <../searchd_program_configuration_options/attrflush_period.html>`__
   setting

-  fixed #1244, per-API-command (search, update, etc) statistics were
   not updated by SphinxQL requests

-  fixed #1243, misc issues (broken statistics, weights, checks) with
   very long keywords having blended parts in RT indexes

-  fixed #1240, embedded ``xmlpipe2`` schema with more attributes than
   the ``sphinx.conf`` one caused ``indexer`` to crash

-  fixed #1239, memory leak when optimizing ``ABS(const)`` and other
   1-arg functions

-  fixed #1228, #761, #1183, #1190, #1198, misc issues occasonally
   caused by MVA updates (crash on SaveAttributes; index rotation vs
   index name and TID; looped MVA updates; persistent MVA removal on
   rotation)

-  fixed #1227, API queries with ``SetGeoAnchor()`` were logged
   incorrectly in SphinxQL-format query logs
   (``query_log_format=sphinxql``)

-  fixed #1214, phrase query parsing issues when
   `blend\_chars <../index_configuration_options/blendchars.html>`__
   contained a quote (“) symbol

-  fixed #1213, attribute aliases were not recognized by the subsequent
   ``SELECT`` items

-  fixed #1212, ```indextool`` <../indextool_command_reference.html>`__
   failed to check hitless keywords

-  fixed #1210, crash when indexing an index with joined fields only (no
   regular fields)

-  fixed #1209, ``xmlpipe_fixup_utf8`` off by a byte on certain (pretty
   rare) malformed sequences

-  fixed #1202, various issues with ``CALL KEYWORDS`` vs RT indexes
   (crashes vs ``dict=keywords``, missing modifiers in output)

-  fixed #1201, snippets vs ``query_mode=1`` vs complex OR-queries could
   occasionally crash

-  fixed #1197, ``indexer`` running out of disk space could either
   crash, or fail to display a proper error message

-  fixed #1185, keywords with wildcards were not handled when
   highlighting the entire document

-  fixed #1184, ``indexer`` crash when
   `ngram\_chars <../index_configuration_options/ngramchars.html>`__ was
   set, but
   `ngram\_len=0 <../index_configuration_options/ngramlen.html>`__

-  fixed #1182, ``indexer`` crash on certain combinations of
   ```docinfo=inline`` <../index_configuration_options/docinfo.html>`__ vs
   bitfields

-  fixed #1181, ``GROUP BY`` on a MVA64 was truncated at 32 bits

-  fixed #1179, ``passage_boundary`` in snippets could get ignored (when
   highlighting the entire document)

-  fixed #1178, ``indexer`` could crash when ``charset_table`` specified
   out-of-bounds codes

-  fixed #1177, SPZ queries in snippets erroneously required
   `passage\_boundary <../additional_functionality/buildexcerpts.html>`__
   option to be explicitly set

-  fixed #1176, multi-queries with a ``GROUP/ORDER BY`` on a string
   attributed crashed

-  fixed #1175, connection id mismatch in SphinxQL-format query logs

-  fixed #1167, nested parentheses in a full-text query could mistakenly
   reset preceding field or zone limit operator

-  fixed #1158, float range filters were not supported in a multi-query
   batch optimizer

-  fixed #1157, broken gcc-4.7 build

-  fixed #1156, empty result set instead of an error message when
   querying distributed indexes with compat\_sphinxql\_magic=1 and
   hitting an error

-  fixed #1143, dash after a number incorrectly parsed as an operator
   ``NOT``

-  fixed #1137, ``searchd``
   `–stopwait <../searchd_command_reference.html>`__ hanged when the
   running instance crashed during shutdown

-  fixed #1136, high idle CPU load on systems without
   ``pthread_timed_lock()``

-  fixed #1134, issues with ``prefork`` workers on systems without
   ``pthread_timed_lock()``

-  fixed #1133,
   ```BuildExcerpts()`` <../additional_functionality/buildexcerpts.html>`__
   on a distributed index with ``load_files`` did not distribute the
   jobs

-  fixed #1126, inaccurate hits sorting progress report on joined field
   indexing

-  fixed #1121, occasional bad entries (wrong characters or invalid SQL)
   in SphinxQL-format query log

-  fixed #1118, ``libsphinxclient`` requests failed when using
   ``SPH_RANK_EXPR``

-  fixed #1073, improved handling of wordforms/multiforms rules
   referring to stopwords

-  fixed #1062, bigint filter ranges truncated when searching via
   `SphinxQL <../8_sphinxql_reference/README.html>`__

-  fixed #1052, SphinxSE range arguments with leading zeroes mistakenly
   parsed as octal

-  fixed #1011, negative MVA64 values mistakenly converted to positive
   (on indexing and/or output)

-  fixed #974, crash when logging queries over 2048 bytes with
   performance counters enabled

-  fixed #909, field-end modifier was ignored when followed by a
   non-whitespace syntax character (eg quote or bracket)

-  fixed #907, issue with bigint filtering (large positive or negative
   values)

-  fixed #906, #1074, Mac OS X 10.7.3 builds (conflicting memory
   allocation routines in Sphinx and external libs)

-  fixed #901, #1066, sending bigger request packets was broken in
   Python API

-  fixed #879, filters on weight-dependent expressions did not work
   correctly

-  fixed #553, default/missing port value was not handled properly in
   `SetServer() <../general_api_functions/setserver.html>`__ API call

-  fixed that blended vs multiforms vs
   `min\_word\_len <../index_configuration_options/minword_len.html>`__
   could hang the query parser

-  fixed missing command-line switches documentation
