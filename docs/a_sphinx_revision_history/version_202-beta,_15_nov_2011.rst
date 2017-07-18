Version 2.0.2-beta, 15 nov 2011
-------------------------------

Major new features
~~~~~~~~~~~~~~~~~~

-  added keywords dictionary
   (```dict=keywords`` <../index_configuration_options/dict.rst>`__)
   support to RT indexes

-  added `MVA <../index_configuration_options/rtattr_multi.rst>`__,
   `index\_exact\_words <../index_configuration_options/indexexact_words.rst>`__
   support to RT indexes (#888)

-  added `MVA64 <../mva_multi-valued_attributes.rst>`__ (a set of
   BIGINTs) support to both disk and RT indexes
   (`rt\_attr\_multi\_64 <../index_configuration_options/rtattr_multi_64.rst>`__
   directive)

-  added an `expression-based
   ranker <../search_results_ranking/expression_based_ranker_sphrank_expr.rst>`__,
   and a number of new ranking factors

-  added `ATTACH INDEX <../attach_index_syntax.rst>`__ statement that
   converts a disk index to RT index

-  added ``WHERE`` clause support to `UPDATE <../update_syntax.rst>`__
   statement

-  added ``bigint``, ``float``, and ``MVA`` attribute support to
   `UPDATE <../update_syntax.rst>`__ statement

New features
~~~~~~~~~~~~

-  added support for upto `256 searchable
   fields <../full-text_fields.rst>`__ (was upto 32 before)

-  added
   ```FIBONACCI()`` <../5_searching/expressions,_functions,_and_operators/numeric_functions.rst#expr-func-fibonacci>`__
   function to
   `expressions <../expressions,_functions,_and_operators/README.rst>`__

-  added `load\_files\_scattered
   option <../additional_functionality/buildexcerpts.rst>`__ to snippets

-  added implicit attribute type promotions in multi-index result sets
   (#939)

-  added index names to ``indexer`` progress message on merge (#928)

-  added ```--replay-flags`` <../searchd_command_reference.rst>`__ switch
   to ``searchd``

-  added string attribute support and a few previously missing `snippets
   options <../building_snippets_excerpts_via_mysql.rst>`__ to SphinxSE

-  added previously missing
   ```Status()`` <../additional_functionality/status.rst>`__,
   ```SetConnectTimeout()`` <../general_api_functions/setconnecttimeout.rst>`__
   API calls to Python API

-  added ``ORDER BY RAND()`` support to `SELECT <../select_syntax.rst>`__
   statement

-  added Sphinx version to Windows crash log

-  added RT index support to
   `indextool <../indextool_command_reference.rst>`__ ``--check`` (checks
   disk chunks only) (#877)

-  added ``prefork_rotation_throttle`` directive (preforked children
   restart delay, in milliseconds) (#873)

-  added
   `on\_file\_field\_error <../indexer_program_configuration_options/onfile_field_error.rst>`__
   directive (different ``sql_file_field`` handling modes)

-  added manpages for all the programs

-  added syslog logging support

-  added sentence, paragraph, and zone support in
   ``html_strip_mode=retain`` mode to snippets

-  optimized search performance with many ``ZONE`` operators

-  improved suggestion tool (added Levenshtein limit, removed extra DB
   fetch)

-  improved `sentence
   extraction <../index_configuration_options/indexsp.rst>`__ (handles
   salutations, starting initials better now)

-  changed
   `max\_filter\_values <../searchd_program_configuration_options/maxfilter_values.rst>`__
   sanity check to 10M values

New SphinxQL features
~~~~~~~~~~~~~~~~~~~~~

-  added `FLUSH RTINDEX <../flush_rtindex_syntax.rst>`__ statement

-  added ``dist_threads`` directive (parallel processing),
   ``load_files``, ``load_files_scattered``, batch syntax (multiple
   documents) support to `CALL SNIPPETS <../call_snippets_syntax.rst>`__
   statement

-  added ``OPTION comment=&#039;...&#039;`` support to
   `SELECT <../select_syntax.rst>`__ statement (#944)

-  added `SHOW VARIABLES <../show_variables_syntax.rst>`__ statement

-  added dummy handlers for `SET
   TRANSACTION <../set_transaction_syntax.rst>`__, `SET
   NAMES <../set_syntax.rst>`__, [SELECT @@sysvar](../select\_syntax.rst)
   statements, and for ``sql_auto_is_null``, ``sql_mode``, and @@-style
   variables (like @@tx\_isolation) in `SET <../set_syntax.rst>`__
   statement (better MySQL frameworks/connectors support)

-  added complete `SphinxQL error
   logging <../searchd_query_log_formats/sphinxql_log_format.rst>`__ (all
   errors are logged now, not just ``SELECT``\ s)

-  improved `SELECT <../select_syntax.rst>`__ statement syntax, made
   expressions aliases optional

Bug fixes
~~~~~~~~~

-  fixed #982, empty binlogs prevented upgraded daemon from starting up

-  fixed #978, libsphinxclient build failed on sparc/sparc64 solaris

-  fixed #977, eliminated (most) compiler warnings

-  fixed #969, broken expression MVA/string argument type check
   prevented IF(IN(mva..)) and other valid expressions from working

-  fixed #966, NOT IN @global\_var syntax was not supported

-  fixed #958, mem\_limit over INT\_MAX was not clamped

-  fixed #954, UTF-8 snippets could crash on malformed data

-  fixed #951, UTF-8 snippets could hang on malformed data

-  fixed #947, bad float column type was reported via SphinxQL, breaking
   some clients

-  fixed #940, group-by with a small enough ``max_matches`` limit could
   occasionaly crash and/or sort wrongly

-  fixed #932, sending huge queries to agents occasionally failed
   (mainly on Windows)

-  fixed #926, snippets did not highlight widlcard matches with
   morphology enabled

-  fixed #918, crash logger did not report a proper query in
   ``dist_threads`` case

-  fixed #916, watchdog caused (endless) respawns if there was a crash
   during shutdown

-  fixed #904, attribute names were not forcibly case-folded in some API
   calls (eg. ``SetGroupDistinct``)

-  fixed #902, query parser did not support ``stopword_step=0``

-  fixed #897, network sockets dangled (open but unattended) while
   replaying binlog

-  fixed #855, ``allow_empty`` option in snippets did not always work
   correctly

-  fixed #854, indexing with many ``bigint`` attributes and
   ``docinfo=inline`` crashed

-  fixed #838, RT MVA insertion did not sort MVA values, caused matching
   issues

-  fixed #833, duplicate MVA values were not eliminated on update

-  fixed #832, certain (overshort/incorrect) documents crashed indexing
   MS SQL Unicode columns

-  fixed #829, query parser did not properly handle numerics with
   ``blend_chars``

-  fixed #814, group-by string attributes in RT indexes dit not always
   work correctly

-  fixed #812, utf8 stemming produced unexpected stems on words with
   single-byte chars

-  fixed #808, huge queries crashed logging with
   ``query_log_format=sphinxql``

-  fixed #806, stray single-star keyword crashed on querying

-  fixed #798, snippets ignored ``index_exact_words`` in query\_mode

-  fixed #797, RT klist loader had an occasional off-by-one crash

-  fixed #791, ``preopen_indexes`` erroneously defaulted to 0 on Windows

-  fixed #790, huge dictionaries (over 4 GB) did not work

-  fixed #786, ``inplace_enable`` could occasionally corrupt the indexes

-  fixed #775, doc had a typo (soundex vs metaphone)

-  fixed #772, snippets duplicated blended chars on a SPZ boundary

-  fixed #762, query parser truncated digit-only keywords over 15 digits

-  fixed #736, query parser dit not properly handle blended/special char
   sequence

-  fixed #726, rotation of an index with a changed attribute count
   crashed

-  fixed #687, querying multiple indexes with index weights and sort-by
   expression produced incorrect (unadjusted) weights

-  fixed #585, (unsupported) string ordinals were silently zeroed out
   with ``docinfo=inline`` (instead of failing)

-  fixed #583, certain keywords could occasionally crash multiforms

-  fixed that concurrent MVA updates could crash

-  fixed that query parser did not ignore a pure blended token with a
   leading modifier

-  fixed that query parser did not properly handle a modifier followed
   by a dash

-  fixed that substring indexing with ``dict=crc`` did not support
   ``index_exact_words`` and ``zones``

-  fixed that in a rare edge case common subtree cache could crash

-  fixed that empty result set returned the full schema (rather than
   ``SELECT``-ed columns)

-  fixed that SphinxQL did not have a sanity check for (currently
   unsupported) result set schemas over 250 attributes

-  fixed that updates on regular indexes were not binlogged

-  fixed that multi-query optimization check for expressions did not
   handle multi-index case

-  fixed that SphinxSE did not build vs MySQL 5.5 release

-  fixed that ``proximity_bm25`` ranker could yield incorrect weight on
   duplicated keywords

-  fixed that prefix expansion with ``dict=keyword`` occasionally
   crashed

-  fixed that ``strip_path`` did not work on RT disk chunks

-  fixed that exclude filters were not properly logged in
   ``query_log_format=sphinxql`` mode

-  fixed that plain string attribute check in ``indextool`` ``--check``
   was broken

-  fixed that Java API did not let specify a connection timeout

-  fixed that ordinal and wordcount attributes could not be fetched via
   SphinxQL

-  fixed that in a rare edge case ``OR/ORDER`` would not match properly

-  fixed that sending (huge) query response did not handle ``EINTR``
   properly

-  fixed that ``SPH04`` ranker could yield incorrectly high weight in
   some cases

-  fixed that C API did not let zero out cutoff, ``max_matches``
   settings

-  fixed that on a persistent connection there were occasionally issues
   handling signals while doing network reads/waitss

-  fixed that in a rare edge case (field start modifier in a certain
   complex query) querying crashed

-  fixed that snippets did not support ``dist_threads`` with
   ``load_files=0``

-  fixed that in some extremely rare edge cases tiny parts of an index
   could end up corrupted with ``dict=keywords``

-  fixed that field/zone conditions were not propagated to expanded
   keywords with ``dict=keywords``
