Version 2.2.2-beta, 11 feb 2014
-------------------------------

New features
~~~~~~~~~~~~

-  added #1604, `CALL KEYWORDS <../call_keywords_syntax.md>`__ can show
   now multiple lemmas for a keyword

-  added `ALTER TABLE DROP COLUMN <../alter_syntax.md>`__

-  added ALTER for JSON/string/MVA attributes

-  added
   `REMAP() <../5_searching/expressions,_functions,_and_operators/miscellaneous_functions.md#expr-func-remap>`__
   function which surpasses SetOverride() API

-  added an argument to
   `PACKEDFACTORS() <../expressions,_functions,_and_operators/miscellaneous_functions.md>`__
   to disable ATC calculation (syntax: PACKEDFACTORS({no\_atc=1}))

-  added exact phrase query syntax

-  added flag ``&#039;--enable-dl&#039;`` to configure script which
   works with ``libmysqlclient``, ``libpostgresql``, ``libexpat``,
   ``libunixobdc``

-  added new plugin system:
   `CREATE <../create_plugin_syntax.md>`__/`DROP
   PLUGIN <../drop_plugin_syntax.md>`__, `SHOW
   PLUGINS <../show_plugins_syntax.md>`__,
   `plugin\_dir <../common_section_configuration_options/plugindir.md>`__
   now in common,
   `index/query\_token\_filter <../create_plugin_syntax.md>`__ plugins

-  added
   `ondisk\_attrs <../index_configuration_options/ondiskattrs.md>`__
   support for RT indexes

-  added position shift operator to phrase operator

-  added possibility to add user-defined rankers (via
   `plugins <../6_extending_sphinx/README.md>`__)

Optimizations, behavior changes, and removals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  changed #1797, per-term statistics report (expanded terms fold to
   their respective substrings)

-  changed default
   `thread\_stack <../searchd_program_configuration_options/threadstack.md>`__
   value to 1M

-  changed local directive in a distributed index which takes now a list
   (eg. ``local=shard1,shard2,shard3``)

-  deprecated
   `SetMatchMode() <../full-text_search_query_settings/setmatchmode.md>`__
   API call

-  deprecated
   `SetOverride() <../general_query_settings/setoverride.md>`__ API call

-  optimized infix searches for dict=keywords

-  optimized kill lists in plain and RT indexes

-  removed deprecated ``&quot;address&quot;`` and ``&quot;port&quot;``
   config keys

-  removed deprecated CLI ``search`` and ``sql_query_info``

-  removed deprecated ``charset_type`` and ``mssql_unicode``

-  removed deprecated ``enable_star``

-  removed deprecated ``ondisk_dict`` and ``ondisk_dict_default``

-  removed deprecated ``str2ordinal`` attributes

-  removed deprecated ``str2wordcount`` attributes

-  removed support for client versions 0.9.6 and below
