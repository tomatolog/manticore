## Version 2.0.9-release, 26 aug 2013 {#version-2-0-9-release-26-aug-2013}

### Bug fixes {#bug-fixes}

*   fixed #1655, special characters like ()?* were not processed correctly by exceptions

*   fixed #1651, [CREATE FUNCTION](../create_function_syntax.md) can now be used with BIGINT return type

*   fixed #1649, incorrect warning message (about statistics mismatch) was returned when mixing wildcards and regular keywords

*   fixed #1603, passing MVA64 arguments to non-MVA functions caused unpredicted behavior and crashes (now explicitly forbidden)

*   fixed #1601, negative numbers in [IN()](../5_searching/expressions,_functions,_and_operators/comparison_functions.md#expr-func-in) clause caused a syntax error

*   fixed #1581, [dict=keywords](../index_configuration_options/dict.md) and [sql_joined_field](../data_source_configuration_options/sqljoined_field.md) occasionally caused `indexer` to build corrupted indexes

*   fixed #1546, file descriptor leaked on index rotation (that eventually prevented `searchd` to reload indexes)

*   fixed #1537, `COUNT(*)` and compat_sphinxql_magics=0 via SphinxAPI caused an incorrect error message

*   fixed #1531, #1589, several matching and highlighting issues when using both [blend_chars](../index_configuration_options/blendchars.md) and multi-wordforms

*   fixed #1521, `indextool --check` did not handle empty RT MVA and gave an incorrect warning

*   fixed #1392, SphinxSE builds with MySQL 5.6 now

*   fixed #1346, [NEAR](../extended_query_syntax.md) handles duplicated keywords properly now

*   fixed #757, wordforms shared between multiple indexes with different tokenizer settings failed to load (they now load with a warning)

*   fixed that batch queries did not batch in some cases (because of internal expression alias issues)

*   fixed that [CALL KEYWORDS](../call_keywords_syntax.md) occasionally gave incorrect error messages

*   fixed searchd crashes on [ATTACHing](../attach_index_syntax.md) plain indexes with MVAs

*   fixed several deadlocks and other threading issues

*   fixed incorrect sorting order with [utf8_general_ci](../collations.md)

*   fixed that in some cases incorrect attribute values were returned when using expression aliases

*   optimized [xmlpipe2](../xmlpipe2_data_source.md) indexing

*   added a warning for missed stopwords, exception, wordforms files on index load and in `indextool --check`