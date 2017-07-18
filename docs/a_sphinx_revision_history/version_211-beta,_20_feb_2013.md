## Version 2.1.1-beta, 20 feb 2013 {#version-2-1-1-beta-20-feb-2013}

### Major new features {#major-new-features}

*   added query profiling (SET PROFILING=1 and [SHOW PROFILE](../show_profile_syntax.md) statements)

*   added AOT-based Russian lemmatizer ([morphology={lemmatize_ru | lemmatize_ru_all}](../index_configuration_options/morphology.md), [lemmatizer_base](../common_section_configuration_options/lemmatizerbase.md), and [lemmatizer_cache](../indexer_program_configuration_options/lemmatizercache.md) directives)

*   added [wordbreaker](../wordbreaker_command_reference.md), a tool to split compounds into individual words

*   added JSON attributes support ([sql_attr_json](../data_source_configuration_options/sqlattr_json.md), [on_json_attr_error](../common_section_configuration_options/onjson_attr_error.md), [json_autoconv_numbers](../common_section_configuration_options/jsonautoconv_numbers.md), [json_autoconv_keynames](../common_section_configuration_options/jsonautoconv_keynames.md) directives)

*   added initial subselects support, SELECT * FROM (SELECT ... ORDER BY cond1 LIMIT X) ORDER BY cond2 LIMIT Y

*   added bigram indexing, and phrase searching with bigrams ([bigram_index](../index_configuration_options/bigramindex.md), [bigram_freq_words](../index_configuration_options/bigramfreq_words.md) directives)

*   added HA/LB support, ha_strategy and agent_persistent directives, SHOW AGENT STATUS statement

*   added RT index optimization ([OPTIMIZE INDEX](../optimize_index_syntax.md) statement, [rt_merge_iops](../searchd_program_configuration_options/rtmerge_iops.md) and [rt_merge_maxiosize](../searchd_program_configuration_options/rtmerge_maxiosize.md) directives)

*   added wildcards support to [dict=keywords](../index_configuration_options/dict.md) (eg. &quot;t?st*&quot;)

*   added substring search support (min_infix_len=2 and above) to [dict=keywords](../index_configuration_options/dict.md)

### New features {#new-features}

*   added --checkconfig switch to [indextool](../indextool_command_reference.md) to check config file for correctness (bug #1395)

*   added global IDF support ([global_idf](../index_configuration_options/globalidf.md) directive, [OPTION global_idf](../select_syntax.md))

*   added &quot;term1 term2 term3&quot;/0.5 [quorum fraction syntax](../extended_query_syntax.md) (bug #1372)

*   added an option to apply stopwords before morphology, [stopwords_unstemmed](../index_configuration_options/stopwordsunstemmed.md) directive

*   added an alternative method to compute keyword IDFs, [OPTION idf=plain](../select_syntax.md)

*   added boolean query optimizations, [OPTION boolean_simplify=1](../select_syntax.md) (bug #1294)

*   added stringptr return type support to UDFs, and [CREATE FUNCTION ... RETURNS STRING syntax](../create_function_syntax.md)

*   added early query termination by predicted execution time ([OPTION max_predicted_time](../select_syntax.md), and [predicted_time_costs](../searchd_program_configuration_options/predictedtime_costs.md) directive)

*   added [index_field_lengths](../index_configuration_options/indexfield_lengths.md) directive, BM25A() and BM25F() functions to [expression ranker](../search_results_ranking/expression_based_ranker_sphrank_expr.md)

*   added ranker=export, and [PACKEDFACTORS()](../5_searching/expressions,_functions,_and_operators/miscellaneous_functions.md#expr-func-packedfactors) function

*   added [OPTION agent_query_timeout](../select_syntax.md)

*   added support for attribute files over 4 GB (bug #1274)

*   added addr2line output to crash reports (bug #1265)

*   added [OPTION ignore_nonexistent_columns](../update_syntax.md) to UPDATE, and a respective [UpdateAttributes()](../additional_functionality/updateattributes.md) argument

*   added --keep-attrs switch to [indexer](../indexer_command_reference.md)

*   added --with-static-mysql, --with-static-pgsql switches to configure

*   added double-buffering for RT [INSERTs](../insert_and_replace_syntax.md) (bug #1200)

*   added --morph, --dumpdict switch to [indextool](../indextool_command_reference.md)

*   added support for multiple wordforms files, comment syntax, and pre/post-morphology [wordforms](../index_configuration_options/wordforms.md)

*   added [ZONESPANLIST()](../select_syntax.md) builtin function

*   added [regexp_filter](../index_configuration_options/regexpfilter.md) directive, regexp document/query filtering support (uses RE2)

*   added min_idf, max_idf, sum_idf [ranking factors](../search_results_ranking/expression_based_ranker_sphrank_expr.md)

*   added uservars persistence, and [sphinxql_state](../searchd_program_configuration_options/sphinxqlstate.md) directive (bug #1132)

*   added [POLY2D](../5_searching/expressions,_functions,_and_operators/numeric_functions.md#expr-func-poly2d), [GEOPOLY2D](../5_searching/expressions,_functions,_and_operators/numeric_functions.md#expr-func-geopoly2d), [CONTAINS](../5_searching/expressions,_functions,_and_operators/numeric_functions.md#expr-func-contains) functions

*   added [ZONESPAN](../extended_query_syntax.md) operator

*   added [snippets_file_prefix](../searchd_program_configuration_options/snippetsfile_prefix.md) directive

*   added Arabic stemmer, [morphology=stem_ar](../index_configuration_options/morphology.md) directive (bug #519)

*   added [OPTION sort_method={pq | kbuffer}](../select_syntax.md), an alternative match sorting method

*   added SPZ ([sentence, paragraph](../index_configuration_options/indexsp.md), [zone](../index_configuration_options/indexzones.md)) support to RT indexes

*   added support for upto 255 keywords in [quorum operator](../extended_query_syntax.md) (bug #1030)

*   added multi-threaded agent querying (bug #1000)

### New SphinxQL features {#new-sphinxql-features}

*   added [SHOW INDEX indexname STATUS](../show_index_status_syntax.md) statement

*   added LIKE clause support to multiple SHOW xxx statements

*   added [SNIPPET()](../select_syntax.md) function

*   added [GROUP_CONCAT()](../select_syntax.md) aggregate function

*   added [GROUPBY()](../select_syntax.md) builtin function

*   added iostats and cpustats to [SHOW META](../show_meta_syntax.md)

*   added support for [DELETE](../delete_syntax.md) statement over distributed indexes (bug #1104)

*   added [EXIST(&#039;attr_name&#039;, default_value)](../select_syntax.md) builtin function (bug #1037)

*   added [SHOW VARIABLES WHERE variable_name=&#039;xxx&#039;](../show_variables_syntax.md) syntax

*   added [TRUNCATE RTINDEX](../truncate_rtindex_syntax.md) statement

### Major behavior changes and optimizations {#major-behavior-changes-and-optimizations}

*   changed that UDFs are now allowed in fork/prefork modes via [sphinxql_state](../searchd_program_configuration_options/sphinxqlstate.md) startup script

*   changed that compat_sphinxql_magics now defaults to 0

*   changed that small enough exceptions, wordforms, stopwords files are now embedded into the index header

*   changed that [rt_mem_limit](../index_configuration_options/rtmem_limit.md) can now be over 2 GB (bug #1059)

*   optimized tokenizer (upto 1.25x indexing and snippets speedup)

*   optimized multi-keyword searching (added skiplists)

*   optimized filtering and scan in several frequent cases (single-value, 2-arg, 3-arg WHERE clauses)