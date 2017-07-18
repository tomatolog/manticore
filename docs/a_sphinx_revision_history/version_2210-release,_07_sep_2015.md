## Version 2.2.10-release, 07 sep 2015 {#version-2-2-10-release-07-sep-2015}

### New features and changes {#new-features-and-changes}

*   added #2310, `--replay-flags=ignore-open-errors` switch to replay binlogs even if some files are missing

*   added #2234, support for empty string values (stringattr=&#039;&#039;) in [WHERE](../select_syntax.md) clause

*   added #2233, support for `IN()` filters with string values

*   added #2232, string collation support in [SELECT](../select_syntax.md) expressions

*   added #2121, &quot;where flt&lt;&gt;val&quot; support, &quot;where fltcol=intval&quot; and &quot;where fltcol!=intval&quot; conditions

*   added #2119, new `indexer` exit code 2 on a `--rotate` failure

*   fixed #2207, unified `min_prefix_len`, `min_infix_len` behavior between RT and plain indexes

*   fixed #2020, unified (and greatly shortened) the list of SphinxQL [reserved keywords](../list_of_sphinxql_reserved_keywords.md) between indexer checks, SphinxQL parser checks, and the documentation

### Major bug fixes {#major-bug-fixes}

*   fixed #2251, expressions dependent on aggregation results (eg. as in SELECT MAX(id) m1, m1+10 m2) were not computed properly in RT indexes

*   fixed #2248, [LENGTH()](../5_searching/expressions,_functions,_and_operators/miscellaneous_functions.md#expr-func-length) was 2x off for 64-bit MVA attributes

*   fixed #2146, [OPTIMIZE](../optimize_index_syntax.md) could occasionally break big RT indexes (by violating 4/16 GB string/MVA per chunk size limits)

*   fixed #2118, multi-wordforms with clashing prefixes were processed in a wrong order

*   fixed #1926, disabled and later re-enabled indexes were not picked up again by `searchd` on SIGHUP

### Minor bug fixes {#minor-bug-fixes}

*   fixed #2312, using FACTORS() along with a subtree cache could crash (because on wrong qpos values from the cache passed to the ranker)

*   fixed #2310, comparing a non-existent JSON field with a string constant (as in jcol.some_typo=&#039;abc&#039;) could crash

*   fixed #2309, UDFs with BIGINT return were saved without a type into sphinxql_state file

*   fixed #2305, punctuation chars not mentioned in [charset_table](../index_configuration_options/charsettable.md) could still occasionally affect term position in the query

*   fixed #2303, a combination of [hitless_words](../index_configuration_options/hitlesswords.md), lemmatizer_all, and a phrase operator could match a wrong result set

*   fixed #2301, `searchd` could sometimes crash on shutdown (at pid file unlink()) if the config was reloaded

*   fixed #2296, wordforms with multiple destination tokens broke snippet highlighting

*   fixed #2290, error in the middle of a multi-query batch did not abort SphinxQL packet, causing problems with some MySQL drivers like PHP mysqlnd

*   fixed #2286, multi-quries with different string filters were incorrectly considered identical

*   fixed #2280, HTML stripper incorrectly parsed hexadecimal NCRs (like eg. #xC0)

*   fixed #2273, a bit better error message when OPTIMIZE fails on a too big chunk

*   fixed #2258, some ranking FACTORS() were off when lemmatizer expansions yielded duplicate terms

*   fixed #2257, OR operator over conditional operators could crash

*   fixed #2242, added whitespaces support to SNIPPET() before_match/after_matches options, and fixed the handling of repeated %PASSAGE_ID% macros

*   fixed #2238, added a few safeguards to prevent crashes/freezes on loading damaged RT RAM chunks

*   fixed #2237, ATTACH-ing a part of a distributed index did not correctly invalidate it, could crash

*   fixed #2235, [UPDATE](../update_syntax.md) ... OPTION `strict=1` did not with plain indexes

*   fixed #2225, `searchd` crashed on startup if agent host string was empty

*   fixed #2127, `indextool` did not handle RT indexes with updated JSON attributes in them

*   fixed #2117, [GEODIST()](../5_searching/sorting_modes.md#sph-sort-expr-mode) calls with hash {in=deg,out=mi} arguments on a distributed index did not parse correctly

*   fixed #2113, @@relaxed could occasonally crash ceratin complex queries

*   fixed #2106, using GROUP N BY with a custom ranker and FACTORS() caused crashes and memory leaks

*   fixed #2093, wildcard character at the end of the keyword could sometimes erroneously produce no matches

*   fixed #2088, NEAR operator with NOT argument could crash

*   fixed #1929, allowed `123abc` column names in SphinxQL SELECT (alas, they are still allowed in `indexer`)

*   fixed #1889, #1890, #1891, a few typo-style bugs in `libsphinxclient` sphinx_set_field_weights(), sphinx_set_index_weights(), sphinx_add_filter_entry()

*   fixed #1859, #2202, XML/TSV/CSV sources now works with control characters like EOF, and UTF BOM marks

*   fixed #1815, a number of SphinxSE issues (inet adress endpoint, too big numbers at MVA, and MVA inserts/replaces via SphinxQL)

*   fixed #1704, [CONTAINS()](../5_searching/expressions,_functions,_and_operators/numeric_functions.md#expr-func-contains) now correctly handles polygons with duplicated points

*   fixed #1643, [CRC32()](../5_searching/expressions,_functions,_and_operators/miscellaneous_functions.md#expr-func-crc32) is now properly evaluated as unsigned in BIGINT context

*   fixed #1567, #1747, #2245, column name quotation could fail in UDF expressions and distributed queries

*   fixed #1551, off-by-one blended keyword position errors in proximity queries (phrase, NEAR, etc)

*   fixed #1528, metaphone on too long (eg. Chinese or Japanese) strings crashed with a buffer overflow

*   fixed #1510, added an unknown field warning to SetFieldWeights() API call and SphinxQL OPTION field_weights

*   fixed #1367, remote agents (in distributed index) could not be accessed via UNIX sockets

*   fixed #1349, max_matches=0 was not handled correctly in `libsphinxclient` sphinx_set_limits()

*   fixed Github PR-1, SphinxSE TLS leak on table reopen

*   fixed `searchd` crash when trying to load a damaged index with an incorrect row count

*   fixed `indextool` MVA checks (an index error could sometimes be mistakenly reported)