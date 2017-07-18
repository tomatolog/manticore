Version 2.2.4-release, 11 sep 2014
----------------------------------

New major features
~~~~~~~~~~~~~~~~~~

-  added `ALTER <../alter_syntax.md>`__ RTINDEX rt1 RECONFIGURE which
   allows to change RT index settings on the fly

-  added `SHOW INDEX idx1 SETTINGS <../show_index_settings_syntax.md>`__
   statement

-  added ability to specify several destination forms for the same
   source wordform (as a result, N:M mapping is now available)

-  added blended chars support to exceptions

New minor features
~~~~~~~~~~~~~~~~~~

-  added
   `ANY() <../5_searching/expressions,_functions,_and_operators/miscellaneous_functions.md#expr-func-any>`__/`ALL() <../5_searching/expressions,_functions,_and_operators/miscellaneous_functions.md#expr-func-all>`__/`INDEXOF() <../5_searching/expressions,_functions,_and_operators/miscellaneous_functions.md#expr-func-indexof>`__
   support for JSON string arrays

-  added FACTORS() alias for
   `PACKEDFACTORS() <../5_searching/expressions,_functions,_and_operators/miscellaneous_functions.md#expr-func-packedfactors>`__
   function

-  added ``LIMIT`` clause for the `FACET <../select_syntax.md>`__
   keyword

-  added JSON-formatted output to ``PACKEDFACTORS()`` function

-  added #1999
   `ATAN2() <../5_searching/expressions,_functions,_and_operators/miscellaneous_functions.md#expr-func-atan2>`__
   function

-  added connections counter and also avg and max timers to agent status

-  added ``searchd`` configuration keys
   `agent\_connect\_timeout <../searchd_program_configuration_options/agentconnect_timeout.md>`__,
   `agent\_query\_timeout <../searchd_program_configuration_options/agentquery_timeout.md>`__,
   `agent\_retry\_count <../searchd_program_configuration_options/agentretry_count.md>`__
   and
   `agent\_retry\_delay <../searchd_program_configuration_options/agentretry_delay.md>`__

-  `GROUPBY() <../select_syntax.md>`__ function now returns strings for
   string attributes

Optimizations and removals
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  optimized
   `json\_autoconv\_numbers <../common_section_configuration_options/jsonautoconv_numbers.md>`__
   option speed

-  optimized tokenizing with expections on

-  fixed #1970, speeding up `ZONE and
   ZONESPAN <../extended_query_syntax.md>`__ operators

Bug fixes
~~~~~~~~~

-  fixed #2027, slow queries to multiple indexes with large kill-lists

-  fixed #2022, blend characters of matched word must not be outside of
   snippet passage

-  fixed #2021, output units in
   `GEODIST() <../5_searching/expressions,_functions,_and_operators/miscellaneous_functions.md#expr-func-geodist>`__
   function

-  fixed #2018, different wildcard behaviour in RT and plain indexes

-  fixed #2005, aggregate functions improperly calculate aliased
   expressions

-  fixed #1972, daemon crashes trying to read a big (>8G) .spm file

-  fixed #1966,
   `INTERVAL() <../5_searching/expressions,_functions,_and_operators/comparison_functions.md#expr-func-interval>`__
   function does not work with JSON fields

-  fixed #1963, ``GROUPBY()`` on JSON attributes sometimes yields NULL

-  fixed ``GROUPBY()`` on empty JSON arrays to return NULL instead of []

-  fixed buffer overrun when sizing packed factors (with way too many
   fields) in expression ranker

-  fixed cpu time logging for cases where work is done in child threads
   or agents
