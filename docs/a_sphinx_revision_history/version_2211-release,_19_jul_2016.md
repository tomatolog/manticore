## Version 2.2.11-release, 19 jul 2016 {#version-2-2-11-release-19-jul-2016}

### Bug fixes {#bug-fixes}

*   fixed #2499 crash of daemon at phrase node with star shift; added regressions to test 41

*   Backported RE2 patch and solutions from master

*   fixed #2488 performance issue with matching hitless terms

*   fixed #2498 wrong profiling report (was filter instead get_hits)

*   fixed #2497 windows service does not handle system shutdown

*   fixed #2484 plugin ranker at distributed index, crash of daemon in case no plugin at agent and check of cache

*   fixed #2495 filtering by false/true/null values without using aliases

*   fixed #2484 plugin ranker and token_filter work with distributed index; set master ver to 14

*   fixed #2485 client failed to parse reply with string_ptr attribute via API; added regression to test 159

*   fixed #2462 added OPTION statements to SphinxQL log fixed string split buffer overrun

*   fixed #2458 expression with escaped quote was cut at distributed index; added regressions to test 125

*   fixed #2459 incorrect indexer exit code for indexing multiple indexes

*   fixed #2452 group by aliased JSON array

*   optimized sphWildcardMatch (UTF-8 vs ASCII)

*   fixed #2451 UTF-8 support for extended wildcards (?, %)

*   fixed #2434 multiple declaration of same attribute breaks *sv pipe data sources and index; added test 257

*   fixed #2437 64-bit values comparison for ALL/ANY/INDEXOF functions

*   fixed #2434 field modifier error for over-short word; added regression to test 211

*   fixed #2435 added HAVING statement to sphinxql query log

*   fixed #2433 crash of indexer for csv source with escaped quote inside quotation; added regression to tests

*   fixed #2431 indexer crash on multiple escape chars at csv source; added regression to tests

*   backported svn:r5092 git:3b5bf10bb852e992f4e02d6f379899413549b5fe

*   fixed #2429 crash of service threads has no crash log

*   fixed #2416 crash of daemon on hit stream with wrong qpos; fixed tests 184, 251

*   fixed #2427 no warnings for short wildcards inside word; added regressions to test 173

*   fixed #2420 count(*) statement vs space characters at facet; added cases to test 226

*   fixed #2209 prohibited order by MVA, backported from master, added error message; fixed tests 20, 180

*   fixed #2419 ATTACH RT index missed doc-id duplicates for id32; fixed test 187

*   fixed #2421 daemon crash on complex query with field start and quorum operators

*   fixed #2417 destination wordform from multiform was stemmed; added regressions to test 22

*   fixed #2419 ATTACH RT index missed doc-id duplicates; added regression to test 184

*   fixed #2418 wildcards do not work at snippets beside star; added cases to test 40

*   fixed #2406 ALTER RECONFIGURE mess with wordforms due to wrong creation order; added regression to test 255

*   fixed #2405 crash of daemon on quorum query with duplicates from expand_keywords; added regression to test 54

*   fixed #2404 ok reply for ALTER query to missed index; added regression to test 213

*   fixed #2394 multi query with profiling enabled; added statements SET, SHOW PLAN, SHOW profile to multi query; added regression to test 113; fixed ubertest to clean up multi query result sets

*   fixed #2398 lcs calculation for large delta positions; added regression to tests 175, 68

*   fixed #2399 crash of daemon for query with json attribute at HAVING; added regressions to test 171

*   fixed #2397 inplace JSON update for several 64-bit values

*   fixed #1415 (destination tokens in wordforms couldn&#039;t be stopwords)

*   fixed #2315 crash of daemon on rotating config without indexes

*   fixed #14 (github) RT index without any attribute; fixed tests 88, 175, 181, 192

*   fixed #2389 indextool now reports on empty segment of RT index at check mode

*   fixed #2383 wrong indexer exit cqode with nohup option

*   fixed #2365 multiple sysvars support in select statement (for Connector/J 5.1.36+)

*   fixed #2363 ping to bad ha mirror pause accept thread at daemon

*   fixed #2376 json-dependent columns vs is null and order by

*   fixed #2355 result set missed SNIPPET expression calc for query with offset; added regressions to test 143

*   fixed JSON type conversion, fixed memory leak, updated test 206

*   fixed #2375 json field type autoconversion in expressions

*   fixed #2363 ping to bad ha mirror pause accept thread at daemon; fixed missed statistics lock

*   fixed #2373 group by 1-character json field, updated test 206

*   fixed crash log time double setup from previous commit

*   fixed #2363 ping to bad ha mirror pause accept thread at daemon (affects all workers but not prefork), moved ping to a separate thread

*   fixed #2364 case-sensitive fields support for distributed indexes

*   fixed #2361 daemon crash with quorum operator; added warning on replacing quorum operator

*   fixed #2359 agent balancing added tests on balancing fixed ping to affect only counters but not timings fixed network statistics aggregation fixed timeout exit on reading agent reply fixed mirror statistics output to be more consistent added feature log_debug_filter to log only matched messages

*   fixed #2356 added error handling for large (&gt;0x400000 bytes) JSON fields

*   fixed #2348 max_matches option did not affect facet queries

*   fixed #2337 crash of indexer on indexing large data passed regexp_filter; added regression to test 194

*   fixed #2336 field modifiers assigned improperly for query with multi destination wordforms; added regressions to test 22

*   fixed #2341 crash of daemon with memory corruption at query to multiple indexes with pool attributes; added regression to test 159

*   fixed #2339 indexer crashed on lemma length overflow; added regression to test 207

*   fixed #1912 indextool memory usage during check of huge index (skiplist keep on disk and docid list variants to use less memory)

*   added string list filter; set master version to 12, API protocol version to 1.31 fixed #2334 daemon crash on filtering by string column via API; fixed string values IN() filter for distributed index; added regression to tests 60, 125

*   fixed #2296 wrong snippet produced from wordforms with multiple destination tokens and AOT dictionary; added regressions to test 223

*   fixed #1675 ZONESPAN was silently ignored with BEFORE operator, added warning

*   fixed #2329 slow wildcard matching (star vs long terms might took above 100 seconds); added regressions to tests

*   fixed #2323 missed field id at packedfactors with json enabled output; fixed model at test 217

*   fixed test 125, enabled back regression

*   fixed #2325 false positive result of indextool check mode for bad index with crc dictionary

*   fixed #2324 daemon crash on handle query via api with empty select list to indexes with dissimilar structure; added regression to test 113

*   fixed JSON mapping from the previous commit (consumes less memory this way)

*   fixed #2320 rt index crashes on groupby() for large JSON fields

*   fixed indextool --check vs nested JSON objects