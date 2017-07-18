Version 2.1.1-beta, 20 feb 2013
-------------------------------

Major new features
~~~~~~~~~~~~~~~~~~

-  added query profiling (SET PROFILING=1 and `SHOW
   PROFILE <../show_profile_syntax.rst>`__ statements)

-  added AOT-based Russian lemmatizer (`morphology={lemmatize\_ru \|
   lemmatize\_ru\_all} <../index_configuration_options/morphology.rst>`__,
   `lemmatizer\_base <../common_section_configuration_options/lemmatizerbase.rst>`__,
   and
   `lemmatizer\_cache <../indexer_program_configuration_options/lemmatizercache.rst>`__
   directives)

-  added `wordbreaker <../wordbreaker_command_reference.rst>`__, a tool
   to split compounds into individual words

-  added JSON attributes support
   (`sql\_attr\_json <../data_source_configuration_options/sqlattr_json.rst>`__,
   `on\_json\_attr\_error <../common_section_configuration_options/onjson_attr_error.rst>`__,
   `json\_autoconv\_numbers <../common_section_configuration_options/jsonautoconv_numbers.rst>`__,
   `json\_autoconv\_keynames <../common_section_configuration_options/jsonautoconv_keynames.rst>`__
   directives)

-  added initial subselects support, SELECT \* FROM (SELECT … ORDER BY
   cond1 LIMIT X) ORDER BY cond2 LIMIT Y

-  added bigram indexing, and phrase searching with bigrams
   (`bigram\_index <../index_configuration_options/bigramindex.rst>`__,
   `bigram\_freq\_words <../index_configuration_options/bigramfreq_words.rst>`__
   directives)

-  added HA/LB support, ha\_strategy and agent\_persistent directives,
   SHOW AGENT STATUS statement

-  added RT index optimization (`OPTIMIZE
   INDEX <../optimize_index_syntax.rst>`__ statement,
   `rt\_merge\_iops <../searchd_program_configuration_options/rtmerge_iops.rst>`__
   and
   `rt\_merge\_maxiosize <../searchd_program_configuration_options/rtmerge_maxiosize.rst>`__
   directives)

-  added wildcards support to
   `dict=keywords <../index_configuration_options/dict.rst>`__ (eg.
   “t?st\*“)

-  added substring search support (min\_infix\_len=2 and above) to
   `dict=keywords <../index_configuration_options/dict.rst>`__

New features
~~~~~~~~~~~~

-  added –checkconfig switch to
   `indextool <../indextool_command_reference.rst>`__ to check config
   file for correctness (bug #1395)

-  added global IDF support
   (`global\_idf <../index_configuration_options/globalidf.rst>`__
   directive, `OPTION global\_idf <../select_syntax.rst>`__)

-  added “term1 term2 term3”/0.5 `quorum fraction
   syntax <../extended_query_syntax.rst>`__ (bug #1372)

-  added an option to apply stopwords before morphology,
   `stopwords\_unstemmed <../index_configuration_options/stopwordsunstemmed.rst>`__
   directive

-  added an alternative method to compute keyword IDFs, `OPTION
   idf=plain <../select_syntax.rst>`__

-  added boolean query optimizations, `OPTION
   boolean\_simplify=1 <../select_syntax.rst>`__ (bug #1294)

-  added stringptr return type support to UDFs, and `CREATE FUNCTION …
   RETURNS STRING syntax <../create_function_syntax.rst>`__

-  added early query termination by predicted execution time (`OPTION
   max\_predicted\_time <../select_syntax.rst>`__, and
   `predicted\_time\_costs <../searchd_program_configuration_options/predictedtime_costs.rst>`__
   directive)

-  added
   `index\_field\_lengths <../index_configuration_options/indexfield_lengths.rst>`__
   directive, BM25A() and BM25F() functions to `expression
   ranker <../search_results_ranking/expression_based_ranker_sphrank_expr.rst>`__

-  added ranker=export, and
   `PACKEDFACTORS() <../5_searching/expressions,_functions,_and_operators/miscellaneous_functions.rst#expr-func-packedfactors>`__
   function

-  added `OPTION agent\_query\_timeout <../select_syntax.rst>`__

-  added support for attribute files over 4 GB (bug #1274)

-  added addr2line output to crash reports (bug #1265)

-  added `OPTION ignore\_nonexistent\_columns <../update_syntax.rst>`__
   to UPDATE, and a respective
   `UpdateAttributes() <../additional_functionality/updateattributes.rst>`__
   argument

-  added –keep-attrs switch to
   `indexer <../indexer_command_reference.rst>`__

-  added –with-static-mysql, –with-static-pgsql switches to configure

-  added double-buffering for RT
   `INSERTs <../insert_and_replace_syntax.rst>`__ (bug #1200)

-  added –morph, –dumpdict switch to
   `indextool <../indextool_command_reference.rst>`__

-  added support for multiple wordforms files, comment syntax, and
   pre/post-morphology
   `wordforms <../index_configuration_options/wordforms.rst>`__

-  added `ZONESPANLIST() <../select_syntax.rst>`__ builtin function

-  added
   `regexp\_filter <../index_configuration_options/regexpfilter.rst>`__
   directive, regexp document/query filtering support (uses RE2)

-  added min\_idf, max\_idf, sum\_idf `ranking
   factors <../search_results_ranking/expression_based_ranker_sphrank_expr.rst>`__

-  added uservars persistence, and
   `sphinxql\_state <../searchd_program_configuration_options/sphinxqlstate.rst>`__
   directive (bug #1132)

-  added
   `POLY2D <../5_searching/expressions,_functions,_and_operators/numeric_functions.rst#expr-func-poly2d>`__,
   `GEOPOLY2D <../5_searching/expressions,_functions,_and_operators/numeric_functions.rst#expr-func-geopoly2d>`__,
   `CONTAINS <../5_searching/expressions,_functions,_and_operators/numeric_functions.rst#expr-func-contains>`__
   functions

-  added `ZONESPAN <../extended_query_syntax.rst>`__ operator

-  added
   `snippets\_file\_prefix <../searchd_program_configuration_options/snippetsfile_prefix.rst>`__
   directive

-  added Arabic stemmer,
   `morphology=stem\_ar <../index_configuration_options/morphology.rst>`__
   directive (bug #519)

-  added `OPTION sort\_method={pq \| kbuffer} <../select_syntax.rst>`__,
   an alternative match sorting method

-  added SPZ (`sentence,
   paragraph <../index_configuration_options/indexsp.rst>`__,
   `zone <../index_configuration_options/indexzones.rst>`__) support to
   RT indexes

-  added support for upto 255 keywords in `quorum
   operator <../extended_query_syntax.rst>`__ (bug #1030)

-  added multi-threaded agent querying (bug #1000)

New SphinxQL features
~~~~~~~~~~~~~~~~~~~~~

-  added `SHOW INDEX indexname
   STATUS <../show_index_status_syntax.rst>`__ statement

-  added LIKE clause support to multiple SHOW xxx statements

-  added `SNIPPET() <../select_syntax.rst>`__ function

-  added `GROUP\_CONCAT() <../select_syntax.rst>`__ aggregate function

-  added `GROUPBY() <../select_syntax.rst>`__ builtin function

-  added iostats and cpustats to `SHOW META <../show_meta_syntax.rst>`__

-  added support for `DELETE <../delete_syntax.rst>`__ statement over
   distributed indexes (bug #1104)

-  added `EXIST(‘attr\_name’, default\_value) <../select_syntax.rst>`__
   builtin function (bug #1037)

-  added `SHOW VARIABLES WHERE
   variable\_name=‘xxx’ <../show_variables_syntax.rst>`__ syntax

-  added `TRUNCATE RTINDEX <../truncate_rtindex_syntax.rst>`__ statement

Major behavior changes and optimizations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  changed that UDFs are now allowed in fork/prefork modes via
   `sphinxql\_state <../searchd_program_configuration_options/sphinxqlstate.rst>`__
   startup script

-  changed that compat\_sphinxql\_magics now defaults to 0

-  changed that small enough exceptions, wordforms, stopwords files are
   now embedded into the index header

-  changed that
   `rt\_mem\_limit <../index_configuration_options/rtmem_limit.rst>`__
   can now be over 2 GB (bug #1059)

-  optimized tokenizer (upto 1.25x indexing and snippets speedup)

-  optimized multi-keyword searching (added skiplists)

-  optimized filtering and scan in several frequent cases (single-value,
   2-arg, 3-arg WHERE clauses)
