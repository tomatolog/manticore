## Version 2.2.2-beta, 11 feb 2014 {#version-2-2-2-beta-11-feb-2014}

### New features {#new-features}

*   added #1604, [CALL KEYWORDS](../call_keywords_syntax.md) can show now multiple lemmas for a keyword

*   added [ALTER TABLE DROP COLUMN](../alter_syntax.md)

*   added ALTER for JSON/string/MVA attributes

*   added [REMAP()](../5_searching/expressions,_functions,_and_operators/miscellaneous_functions.md#expr-func-remap) function which surpasses SetOverride() API

*   added an argument to [PACKEDFACTORS()](../expressions,_functions,_and_operators/miscellaneous_functions.md) to disable ATC calculation (syntax: PACKEDFACTORS({no_atc=1}))

*   added exact phrase query syntax

*   added flag `&#039;--enable-dl&#039;` to configure script which works with `libmysqlclient`, `libpostgresql`, `libexpat`, `libunixobdc`

*   added new plugin system: [CREATE](../create_plugin_syntax.md)/[DROP PLUGIN](../drop_plugin_syntax.md), [SHOW PLUGINS](../show_plugins_syntax.md), [plugin_dir](../common_section_configuration_options/plugindir.md) now in common, [index/query_token_filter](../create_plugin_syntax.md) plugins

*   added [ondisk_attrs](../index_configuration_options/ondiskattrs.md) support for RT indexes

*   added position shift operator to phrase operator

*   added possibility to add user-defined rankers (via [plugins](../6_extending_sphinx/README.md))

### Optimizations, behavior changes, and removals {#optimizations-behavior-changes-and-removals}

*   changed #1797, per-term statistics report (expanded terms fold to their respective substrings)

*   changed default [thread_stack](../searchd_program_configuration_options/threadstack.md) value to 1M

*   changed local directive in a distributed index which takes now a list (eg. `local=shard1,shard2,shard3`)

*   deprecated [SetMatchMode()](../full-text_search_query_settings/setmatchmode.md) API call

*   deprecated [SetOverride()](../general_query_settings/setoverride.md) API call

*   optimized infix searches for dict=keywords

*   optimized kill lists in plain and RT indexes

*   removed deprecated `&quot;address&quot;` and `&quot;port&quot;` config keys

*   removed deprecated CLI `search` and `sql_query_info`

*   removed deprecated `charset_type` and `mssql_unicode`

*   removed deprecated `enable_star`

*   removed deprecated `ondisk_dict` and `ondisk_dict_default`

*   removed deprecated `str2ordinal` attributes

*   removed deprecated `str2wordcount` attributes

*   removed support for client versions 0.9.6 and below