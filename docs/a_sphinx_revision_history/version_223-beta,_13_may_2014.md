## Version 2.2.3-beta, 13 may 2014 {#version-2-2-3-beta-13-may-2014}

### New features {#new-features}

*   added [#1920](http://sphinxsearch.com/bugs/view.php?id=1920), [charset_table](../index_configuration_options/charsettable.md) aliases

*   added [#1887](http://sphinxsearch.com/bugs/view.php?id=1887), filtering over string attributes

*   added [#1860](http://sphinxsearch.com/bugs/view.php?id=1860), [USERVARs](../set_syntax.md) for distributed indexes

*   added [#1689](http://sphinxsearch.com/bugs/view.php?id=1689), [GROUP BY JSON](../select_syntax.md) attributes

*   added [FACET](../select_syntax.md) keyword

*   added Go MySQL connector support

*   added [IDF boost](../extended_query_syntax.md) keyword modifier

*   added [MAYBE](../extended_query_syntax.md) fulltext operator

### Optimizations and removals {#optimizations-and-removals}

*   improved speed of concurrent insertion in RT indexes

*   removed [max_matches](../sphinx_deprecations_and_changes_in_default_configu.md) config key

### Bug fixes {#bug-fixes}

*   fixed #1946, [IN()](../5_searching/expressions,_functions,_and_operators/comparison_functions.md#expr-func-in) function support for string attributes

*   fixed #1942, crash in [SHOW THREADS](../show_threads_syntax.md) command

*   fixed #1922, crash on snippet generation for queries with duplicated words

*   fixed #1919, [TSV](../tsvpipecsvpipe_tabcomma_separated_values_data_sour.md) bitcount attributes indexation issue

*   fixed #1916, [COUNT(*)](../select_syntax.md) with empty result set

*   fixed #1910, JSON parsing issue

*   fixed #1906, [ZONE](../extended_query_syntax.md) constraints for expanded terms

*   fixed #1904, race condition in RT indexes on saving disk chunk

*   fixed #1899, crash on [CALL KEYWORDS](../call_keywords_syntax.md)

*   fixed #1893, `searchd` crashes on expressions like &#039;a&lt;&lt;(*!b)&#039;

*   fixed #1884, crash with [SNIPPET()](../select_syntax.md) function over distributed index

*   fixed #1883, crash at expanded keyword with hitless index

*   fixed #1870, crash on [ORDER BY JSON](../select_syntax.md) attributes

*   fixed template index removing on rotation