Version 2.1.1-beta, 20 feb 2013
-------------------------------

Major new features
~~~~~~~~~~~~~~~~~~

-  added query profiling (SET PROFILING=1 and `SHOW
   PROFILE <../show_profile_syntax.html>`__ statements)

-  added AOT-based Russian lemmatizer (`morphology={lemmatize\_ru \|
   lemmatize\_ru\_all} <../index_configuration_options/morphology.html>`__,
   `lemmatizer\_base <../common_section_configuration_options/lemmatizerbase.html>`__,
   and
   `lemmatizer\_cache <../indexer_program_configuration_options/lemmatizercache.html>`__
   directives)

-  added `wordbreaker <../wordbreaker_command_reference.html>`__, a tool
   to split compounds into individual words

-  added JSON attributes support
   (`sql\_attr\_json <../data_source_configuration_options/sqlattr_json.html>`__,
   `on\_json\_attr\_error <../common_section_configuration_options/onjson_attr_error.html>`__,
   `json\_autoconv\_numbers <../common_section_configuration_options/jsonautoconv_numbers.html>`__,
   `json\_autoconv\_keynames <../common_section_configuration_options/jsonautoconv_keynames.html>`__
   directives)

-  added initial subselects support, SELECT \* FROM (SELECT … ORDER BY
   cond1 LIMIT X) ORDER BY cond2 LIMIT Y

-  added bigram indexing, and phrase searching with bigrams
   (`bigram\_index <../index_configuration_options/bigramindex.html>`__,
   `bigram\_freq\_words <../index_configuration_options/bigramfreq_words.html>`__
   directives)

-  added HA/LB support, ha\_strategy and agent\_persistent directives,
   SHOW AGENT STATUS statement

-  added RT index optimization (`OPTIMIZE
   INDEX <../optimize_index_syntax.html>`__ statement,
   `rt\_merge\_iops <../searchd_program_configuration_options/rtmerge_iops.html>`__
   and
   `rt\_merge\_maxiosize <../searchd_program_configuration_options/rtmerge_maxiosize.html>`__
   directives)

-  added wildcards support to
   `dict=keywords <../index_configuration_options/dict.html>`__ (eg.
   “t?st\*“)

-  added substring search support (min\_infix\_len=2 and above) to
   `dict=keywords <../index_configuration_options/dict.html>`__

New features
~~~~~~~~~~~~

-  added –checkconfig switch to
   `indextool <../indextool_command_reference.html>`__ to check config
   file for correctness (bug #1395)

-  added global IDF support
   (`global\_idf <../index_configuration_options/globalidf.html>`__
   directive, `OPTION global\_idf <../select_syntax.html>`__)

-  added “term1 term2 term3”/0.5 `quorum fraction
   syntax <../extended_query_syntax.html>`__ (bug #1372)

-  added an option to apply stopwords before morphology,
   `stopwords\_unstemmed <../index_configuration_options/stopwordsunstemmed.html>`__
   directive

-  added an alternative method to compute keyword IDFs, `OPTION
   idf=plain <../select_syntax.html>`__

-  added boolean query optimizations, `OPTION
   boolean\_simplify=1 <../select_syntax.html>`__ (bug #1294)

-  added stringptr return type support to UDFs, and `CREATE FUNCTION …
   RETURNS STRING syntax <../create_function_syntax.html>`__

-  added early query termination by predicted execution time (`OPTION
   max\_predicted\_time <../select_syntax.html>`__, and
   `predicted\_time\_costs <../searchd_program_configuration_options/predictedtime_costs.html>`__
   directive)

-  added
   `index\_field\_lengths <../index_configuration_options/indexfield_lengths.html>`__
   directive, BM25A() and BM25F() functions to `expression
   ranker <../search_results_ranking/expression_based_ranker_sphrank_expr.html>`__

-  added ranker=export, and
   `PACKEDFACTORS() <../5_searching/expressions,_functions,_and_operators/miscellaneous_functions.html#expr-func-packedfactors>`__
   function

-  added `OPTION agent\_query\_timeout <../select_syntax.html>`__

-  added support for attribute files over 4 GB (bug #1274)

-  added addr2line output to crash reports (bug #1265)

-  added `OPTION ignore\_nonexistent\_columns <../update_syntax.html>`__
   to UPDATE, and a respective
   `UpdateAttributes() <../additional_functionality/updateattributes.html>`__
   argument

-  added –keep-attrs switch to
   `indexer <../indexer_command_reference.html>`__

-  added –with-static-mysql, –with-static-pgsql switches to configure

-  added double-buffering for RT
   `INSERTs <../insert_and_replace_syntax.html>`__ (bug #1200)

-  added –morph, –dumpdict switch to
   `indextool <../indextool_command_reference.html>`__

-  added support for multiple wordforms files, comment syntax, and
   pre/post-morphology
   `wordforms <../index_configuration_options/wordforms.html>`__

-  added `ZONESPANLIST() <../select_syntax.html>`__ builtin function

-  added
   `regexp\_filter <../index_configuration_options/regexpfilter.html>`__
   directive, regexp document/query filtering support (uses RE2)

-  added min\_idf, max\_idf, sum\_idf `ranking
   factors <../search_results_ranking/expression_based_ranker_sphrank_expr.html>`__

-  added uservars persistence, and
   `sphinxql\_state <../searchd_program_configuration_options/sphinxqlstate.html>`__
   directive (bug #1132)

-  added
   `POLY2D <../5_searching/expressions,_functions,_and_operators/numeric_functions.html#expr-func-poly2d>`__,
   `GEOPOLY2D <../5_searching/expressions,_functions,_and_operators/numeric_functions.html#expr-func-geopoly2d>`__,
   `CONTAINS <../5_searching/expressions,_functions,_and_operators/numeric_functions.html#expr-func-contains>`__
   functions

-  added `ZONESPAN <../extended_query_syntax.html>`__ operator

-  added
   `snippets\_file\_prefix <../searchd_program_configuration_options/snippetsfile_prefix.html>`__
   directive

-  added Arabic stemmer,
   `morphology=stem\_ar <../index_configuration_options/morphology.html>`__
   directive (bug #519)

-  added `OPTION sort\_method={pq \| kbuffer} <../select_syntax.html>`__,
   an alternative match sorting method

-  added SPZ (`sentence,
   paragraph <../index_configuration_options/indexsp.html>`__,
   `zone <../index_configuration_options/indexzones.html>`__) support to
   RT indexes

-  added support for upto 255 keywords in `quorum
   operator <../extended_query_syntax.html>`__ (bug #1030)

-  added multi-threaded agent querying (bug #1000)

New SphinxQL features
~~~~~~~~~~~~~~~~~~~~~

-  added `SHOW INDEX indexname
   STATUS <../show_index_status_syntax.html>`__ statement

-  added LIKE clause support to multiple SHOW xxx statements

-  added `SNIPPET() <../select_syntax.html>`__ function

-  added `GROUP\_CONCAT() <../select_syntax.html>`__ aggregate function

-  added `GROUPBY() <../select_syntax.html>`__ builtin function

-  added iostats and cpustats to `SHOW META <../show_meta_syntax.html>`__

-  added support for `DELETE <../delete_syntax.html>`__ statement over
   distributed indexes (bug #1104)

-  added `EXIST(‘attr\_name’, default\_value) <../select_syntax.html>`__
   builtin function (bug #1037)

-  added `SHOW VARIABLES WHERE
   variable\_name=‘xxx’ <../show_variables_syntax.html>`__ syntax

-  added `TRUNCATE RTINDEX <../truncate_rtindex_syntax.html>`__ statement

Major behavior changes and optimizations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  changed that UDFs are now allowed in fork/prefork modes via
   `sphinxql\_state <../searchd_program_configuration_options/sphinxqlstate.html>`__
   startup script

-  changed that compat\_sphinxql\_magics now defaults to 0

-  changed that small enough exceptions, wordforms, stopwords files are
   now embedded into the index header

-  changed that
   `rt\_mem\_limit <../index_configuration_options/rtmem_limit.html>`__
   can now be over 2 GB (bug #1059)

-  optimized tokenizer (upto 1.25x indexing and snippets speedup)

-  optimized multi-keyword searching (added skiplists)

-  optimized filtering and scan in several frequent cases (single-value,
   2-arg, 3-arg WHERE clauses)
