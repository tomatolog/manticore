## Version 2.1.7-release, 30 mar 2014 {#version-2-1-7-release-30-mar-2014}

### Bug fixes {#bug-fixes}

*   fixed #1917, field limit propagation outside of group

*   fixed #1915, exact form passes to index skipping stopwords filter

*   fixed #1905, multiple lemmas at the end of a field

*   fixed #1903, `indextool` check mode for hitless indexes and indexes with large amount of documents

*   fixed #1902, crash on JSON field in the [IN()](../5_searching/expressions,_functions,_and_operators/comparison_functions.md#expr-func-in) function

*   fixed #1884, crash at [SNIPPET()](../select_syntax.md) with local indexes at distributed index

*   fixed #1802, loading large keywords dictionary

*   fixed #1786, `indextool` fails to handle indexes with AOT morphology

*   fixed crash of daemon on logging extra large message

*   fixed expression engine: division by zero, log and sqrt() functions of non-positive arguments

*   fixed LCS and min_best_span_pos computation

*   fixed unnecessary escaping in JSON result set

*   fixed Quick Tour documentation chapter