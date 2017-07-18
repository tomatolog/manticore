## Version 2.2.7-release, 20 jan 2015 {#version-2-2-7-release-20-jan-2015}

### Minor features {#minor-features}

*   added #2112, string equal comparison support for [IF()](../5_searching/expressions,_functions,_and_operators/comparison_functions.md#expr-func-if) function (for JSON and string attributes)

*   added #2153, [IN()](../5_searching/expressions,_functions,_and_operators/comparison_functions.md#expr-func-in) support for mixed and top-level JSON arrays

### Bug fixes {#bug-fixes}

*   fixed #2158, crash at RT index after morphology changed to AOT after index was created

*   fixed #2155, [stopwords](../index_configuration_options/stopwords.md) got missed on disk chunk save at RT index

*   fixed #2151, agents statistics missed in case of huge amount of agents

*   fixed #2139, escape all special characters in JSON result set, according to RFC 4627

*   fixed #2123, no pid file created in x64 release built with vs2012

*   fixed #2115, `indexer` crash on wordforms with multiple destination keywords

*   fixed #2050, multi result set doesn&#039;t work without `libmysqlclient`

*   fixed #2003, [lemmatize_XX_all](../index_configuration_options/morphology.md) handling of short and exact words

*   fixed #1912, reduce `indextool` memory usage during a check of a huge index

*   fixed off by one errors in filtering of `BIGINT` attributes

*   fixed seamless rotation in [prefork](../searchd_program_configuration_options/workers.md) mode

*   fixed snippets crash with [blend chars](../index_configuration_options/blendchars.md) at the beginning of a string