## Version 2.0.10-release, 22 jan 2014 {#version-2-0-10-release-22-jan-2014}

### Bug fixes {#bug-fixes}

*   fixed #1778, [SENTENCE and PARAGRAPH](../extended_query_syntax.md) operators and infix stars clash

*   fixed #1774, stack overflow on parsing large expressions

*   fixed #1744, daemon failed to write to log file bigger than 4G

*   fixed #1705, expression ranker handling of indexes with more than 32 fields

*   fixed #1700, crash and cutoff in fullscan [reverse_scan=1](../select_syntax.md) queries

*   fixed #1698, proper handling of stopword with blended chars

*   fixed #1682, field end modifier and [index_exact_words](../index_configuration_options/indexexact_words.md) clash

*   fixed #1678, memory leak in SUM() function of an expression ranker

*   fixed #1670, updating of MVA attributes in distributed indexes via API

*   fixed #1662, [EscapeString()](../additional_functionality/escapestring.md) API escapes &#039;&lt;&#039; too now

*   fixed #1520, [SetLimits()](../general_query_settings/setlimits.md) API documentation

*   fixed #1491, documentation: space character is prohibited in [charset_table](../index_configuration_options/charsettable.md)

*   fixed memory leak in expressions with max_window_hits

*   fixed [rt_flush_period](../searchd_program_configuration_options/rtflush_period.md) - less stricter internal check and more often flushes overall