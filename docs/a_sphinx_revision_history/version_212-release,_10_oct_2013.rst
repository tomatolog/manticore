Version 2.1.2-release, 10 oct 2013
----------------------------------

New features
~~~~~~~~~~~~

-  added `FLUSH RAMCHUNK <../flush_ramchunk_syntax.md>`__ statement

-  added `SHOW PLAN <../show_plan_syntax.md>`__ statement

-  added support for `GROUP BY <../select_syntax.md>`__ on multiple
   attributes

-  added
   `BM25F() <../search_results_ranking/expression_based_ranker_sphrank_expr.md>`__
   function to ``SELECT`` expressions (now works with the expression
   based ranker)

-  added `indextool <../indextool_command_reference.md>`__ ``--fold``
   command and ``-q`` switch

-  added JSON debug check for RT index RAM chunk

-  added
   `LENGTH() <../5_searching/expressions,_functions,_and_operators/miscellaneous_functions.md#expr-func-length>`__
   function for MVA

-  added missing
   `rt\_attr\_bool <../index_configuration_options/rtattr_bool.md>`__
   directive

-  added support for selecting over 250 columns via ManticoreQL

-  deprecated custom sort mode, and ``str2ordinal`` and
   ``str2wordcount`` attribute types

-  optimized ``SELECT``, ``UPDATE`` for indexes with many attributes (up
   to 3.5x speedup in extreme cases)

-  ``JSON`` attributes (up to 5-20% faster ``SELECTs`` using JSON
   objects)

-  optimized `xmlpipe2 <../xmlpipe2_data_source.md>`__ indexing (up to 9
   times faster on some schemas)

Bug fixes
~~~~~~~~~

-  fixed #1684, `COUNT(DISTINCT smth) <../select_syntax.md>`__ with
   implicit ``GROUP BY`` returns correct value now

-  fixed #1672, exact token AOT vs lemma (``indexer`` skips exact form
   of token that passed AOT through tokenizer)

-  fixed #1659, fail while loading empty infix dictionary with
   `dict=keywords <../index_configuration_options/dict.md>`__

-  fixed #1638, force explicit JSON type conversion for aggregate
   functions

-  fixed #1628, `GROUP\_CONCAT() <../select_syntax.md>`__ and
   `GROUPBY() <../select_syntax.md>`__ support for distributed agents

-  fixed #1619, ``INTEGER()`` conversion function doesn't support signed
   integers

-  fixed #1615, global IDF vs exact term (=term) fixed global IDF for
   missed terms fixed ManticoreQL `global\_idf=0
   option <../index_configuration_options/globalidf.md>`__

-  fixed #1607, now ignoring binlog when running daemon with
   ``--console`` flag

-  fixed #1606, hard interruption of the daemon by Ctrl+C (SIGINT)
   signal

-  fixed #1592, duplicates vs expression ranker

-  fixed #1578, `SORT BY <../sorting_modes.md>`__ string attribute via
   API ``attr_asc``  ``attr_desc``

-  fixed #1575, crash of daemon on MVA receive from agents with
   `dist\_threads <../searchd_program_configuration_options/distthreads.md>`__
   enabled

-  fixed #1574, agent got kill list of local indexes of distributed
   index

-  fixed #1573, ranker expression vs expanded terms

-  fixed #1572, ``BM25F`` vs negative terms

-  fixed #1550, float got cut at full-text part of a query

-  fixed #1541, ``BM25F`` expression in distributes indexes

-  fixed #1508,
   `#1522 <http://sphinxsearch.com/bugs/view.php?id=1522>`__,
   distributed index query lasts up to
   `agent\_connect\_timeout <../searchd_program_configuration_options/agentconnect_timeout.md>`__
   with epoll path

-  fixed #1508, master failed to connect waiting agents up to
   `agent\_connect\_timeout <../searchd_program_configuration_options/agentconnect_timeout.md>`__
   time

-  fixed #1489, filtering by integer field in JSON using floating point
   precision

-  fixed #1485,
   `index\_exact\_words <../index_configuration_options/indexexact_words.md>`__
   vs keyword dict with infix

-  fixed #1484, `INSERT <../insert_and_replace_syntax.md>`__ into RT vs
   no JSON attribute

-  fixed #1478, memory leaks at daemon
   `PACKEDFACTORS() <../expressions,_functions,_and_operators/miscellaneous_functions.md>`__
   as UDF argument, index query tokenizer, expression ranker SUM()

-  fixed #1470, broken UDF unpack (since r3738 UDF version 2)

-  fixed #1468, multiple conditions in ``WHERE`` for JSON attributes

-  fixed #1466,
   `index\_field\_lengths <../index_configuration_options/indexfield_lengths.md>`__
   vs XML data source

-  fixed #1463, daemon shutdown vs RT index optimize (added forced
   terminate of long merging operation)

-  fixed #1460, `aggregate functions <../select_syntax.md>`__ ``AVG()``,
   ``MAX()``, ``MIN()``, ``SUM()`` do not work for JSON attributes

-  fixed #1459, ``BM25F`` doesn't work with
   `field\_string <../data_source_configuration_options/sqlfield_string.md>`__
   fields

-  fixed #1458, factors to copy ``field_tf`` at UDF

-  fixed #1450, garbage in JSON fields when selecting them from a RT
   index

-  fixed #1449, broken build on Mac OS X

-  fixed #1446, `WEIGHT() <../search_results_ranking/README.md>`__ did
   not work in ``SELECT`` expressions

-  fixed #1445, field-start/field-end modifiers did not work for
   star-expanded keywords

-  fixed #1443,
   `morphology=lemmatizer\_ru\_all <../index_configuration_options/morphology.md>`__
   now works with
   `index\_exact\_words=1 <../index_configuration_options/indexexact_words.md>`__
   (exact forms can be matches)

-  fixed #1442, incorrect ``COUNT(*)`` value in queries to distributed
   indexes with implicit ``GROUP BY``

-  fixed #1439, filters on float values in JSON issue, string values
   quoting issue

-  fixed #1399, filter error message on string attribute

-  fixed #1384, added possibility to define any own DSN line with
   `source=mssql <../data_source_configuration_options/README.md>`__
   (like as in ``source=odbc``)

-  fixed `ATTACH <../attach_index_syntax.md>`__ vs wordforms or
   stopwords; after daemon was restarted this setting was getting lost
   in RT indexes

-  fixed balancing of agents in HA

-  fixed co-working of ``index_exact_word`` + AOT lemmatizer

-  fixed epoll invoking and turned on by default

-  fixed incorrect handling of wildcards in tokenizer

-  fixed infix indexing with ``dict=keywords``

-  fixed `max\_predicted\_time <../select_syntax.md>`__ integer
   overflows

-  fixed memory error in tokenizer

-  fixed several memory leaks

-  fixed ``PACKEDFACTORS()`` to work in different ``GROUP BY`` queries

-  fixed preprocessor definitions for
   `RE2 <../index_configuration_options/regexpfilter.md>`__ in VS
   solution

-  fixed rotation of global IDF for ``workers=threads`` and
   ``seamless_rotate=1``

-  fixed rotation of old indexes

-  fixed RT kill list survives ``TRUNCATE`` and works in newly
   ``ATTACH``\ ed index

-  fixed saving id32 RT index with id64 daemon

-  fixed stemmer vs RT index ``INSERT``

-  fixed string case error with JSON attributes in select list of a
   query

-  fixed ``TOP_COUNT`` usage in ``misc/suggest`` and updated to PHP 5.3
   and UTF-8
