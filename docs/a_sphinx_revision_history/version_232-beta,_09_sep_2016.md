## Version 2.3.2-beta, 09 sep 2016 {#version-2-3-2-beta-09-sep-2016}

### Major features {#major-features}

*   Searchd now uses mmap(). Daemon is available immediately and spawns a separate thread that loads the indexes.
*   Built-in suggest using CALL QSUGGEST statement for indexes with infixing enabled and dict=keywords
*   HTTP protocol interface

### New functions and options {#new-functions-and-options}

*   added RAND(),HOUR(),MINUTE(),SECOND() functions
*   added[FLUSH HOSTNAMES](../flush_hostnames_syntax.md) SphinxQL statement and hostname_lookup directive
*   added [RELOAD INDEX](../reload_index_syntax.md) SphinxQL statement

*   added [sphinxql_timeout](../searchd_program_configuration_options/sphinxqltimeout.md) directive

### Changes and improvements {#changes-and-improvements}

*   changed SHOW INDEX STATUS now displays performed number of queries, query times and found rows of last 1,5,15 minutes and total since daemon start
*   changed retry_count behaviour
*   added wildcard support and new options for CALL KEYWORDS SphinxQL statement
*   faster RT inserts
*   faster CSV/TSV indexing
*   query cache is disabled by default
*   indexer --keeep-attrs support specific path
*   daemon now picks changed index path when it receives HUP
*   added alias support for MVA attributes
*   added SphinxQL support for comparison, IN, and BETWEEN conditions over ANY/ALL(mva)
*   added explicit JSON type conversion in WHERE clause

### Bug fixes {#bug-fixes}

*   fixed #2503 update of attributes at index prevents binlog from clean

*   fixed #2516 suggest for index with exact_word or morphology options

*   fixed #2507 .NET Connector overflow exception (unsigned id support)

*   Fixed initial round-robin counter

*   Thread-safety checks added (backported)

*   Refactored dl-staff

*   added per-index statistics to &#039;show index status&#039;

*   fixed #2502 final calculation of expression at RT index (optimized calls count)

*   Refactored ha-staff

*   Added begin() and end() to CSphVector, CSphTightVector

*   fixed error handle for API protocol net loop

*   Fixed crash on exit (revealed in test 234 on Ubuntu 16.04)

*   added token_filter and string list filter to API (php, python); set client ver to 32; fixed filter string list escape; updated token_filter plugin interface

*   Backported behavior for pthread_mutex_timedlock, SCHED_IDLE

*   Fast runaround for issue #877

*   fixed #2496 profiler counts multiple sequential queries with thread_pool worker

*   fixed #1825 added support for embedded zeroes in fields for pgsql, odbc data sources

*   PHP sphinx api: renamed SphinxClient c-tr to __construct

*   fixed #2461 crash of daemon with worker thread_pool on high load of fast queries

*   fixed uninitialized m_bSync variable

*   fixed #2461 crash of daemon with worker thread_pool on high load of fast queries

*   fixed #2456 daemon stuck on rotating index due to high amount of search threads

*   Fixed internal date calculation which caused different result of day(NUM) function in different timezones

*   fixed #2400 crash of daemon on CALL KEYWORDS to RT index with disk chunks and regexp filter; added regression to test 194

*   added #2393 feature wildcards for CALL KEYWORDS; bunch of options (fold_wildcards, fold_lemmas, fold_blended, expansion_limit, stats); added cases to test 254; fixed github #17

*   fixed #2390 latency at workers thread_pool added net-loop wakeup on job done added send at the end of job then transfer left data to net-loop added spin-wait at polling wait added socket_pair emulation for windows version of net-loop added eventfd checks to configure

*   added length() for expressions, disabled Expr_Time_c hashing, fixed test_253

*   fixed Expr_Time and Expr_Timediff always returning empty strings

*   fixed minor expression hash calc bug

*   added a big test for GetHash in expressions; added Expr_Now_c; fixed template expression name check

*   fixed several filters vs qcache issues

*   check filter expression tree when caching queries

*   fixed #2384 replace large index list at message to distributed index name; added regression to test 153

*   fixed #2384 fold large index list at message from distributed index; added regression to test 153

*   fixed #2372 ALL(mva) filter passed from master to agent as legacy filter; added regressions to test 244; set master version to 13

*   fixed #2371 warning on query via API with filter on MVA attribute; added cases to test 244

*   fixed query cache vs filters with expressions

*   fixed #2351 ALTER RECONFIGURE skipped for RT index with only re2 or rlp changes; added regression as test 252 set binlog version to 6

*   fixed daemon to work with --nodetach option after previous commit breaks it

*   fixed #2358 mmap memory to be fork-less fixed bitvec copying fixing false socket shutdown at net-loop added ping handling to net-loop instead API command added feature to distributed index to break kill-list of local indexes sequence

*   fixed a memory leak on inserts with aot enabled

*   fixed #2062 attribute name shadows field with same name; added check at ALTER and RT index config; added regressions to test 214

*   fixed #2330 daemon shutdown stopped waiting searching threads

*   fixed dlopen bug on linux while reloading udf

*   fixed (searchd.cpp split issues): stats mutex leak and crash of dashboard at distributed index setup due to config reload; added tests 248, 249

*   fixed #2299 crash of indexer due to empty xmlpipe2 source with embedded schema; added regression to test 68

*   fixed RLP vs non-CJK fields (missing trailing zero)

*   refactored RLP to work as a field filter (preprocessor)

*   fixed RLP enabled build

*   fixed ubertest to pass on different linux platforms

*   added SphinxQL support for comparison, IN, and BETWEEN conditions over ANY/ALL(mva); and added missing &quot;ident NOT BETWEEN x AND y&quot; syntax

*   fixed #2277 network connection timeout overflow for agent with worker = thread_pool added test 243

*   fixed mantis-2156 (COUNT(DISTINCT attr) does not work with strings)

*   updated old links to code.google.com to new links to github.com

*   fixed embedded zeroes in rt inserts

*   fixed mantis-1825 (no support for embedded zeroes in fields)

*   Removed CodeBlocks. Modified .gitignore for clion

*   fixed examples version in documentation, rebuilt docs

*   added #2262 new blend_mode trim_all added cases to test 192

*   fixed #2261 ngram chars presence at charset_table, now it warns for such config added regression to tests fixed test 19

*   fixed multiform handling (multiform + lemmatizer case) in CALL KEYWORDS

*   fixed libre2.patch to be in sync with latest re2 changes

*   Eliminated gcc warnings in http_parser.c. Eliminated msvc warning in sphinxquery.cpp.

*   Windows yy.cmd synced with bash yy.sh script

*   lex/bison files and rules fixed for bison &gt;1.875

*   do not create tokenizer for every document in batch insert, create it just once and reuse instead

*   fixed bug #1766 (UPDATE does not correctly update negative values for bigint and float attributes)

*   fixed hits duplicates at RT index on document indexing fixed aggregate depended expression at RT index fixed tests 162, 192, 205 to pass rt mode updated visual studio 2013 project file

*   optimized away crazy memmove() in CSV/TSV parser, much faster CSV/TSV indexing (more than 10x on a synthetic test)

*   field lengths are no longer required to be last in schema

*   initial per-index field lengths support for RT, fixes test 217 --rt

*   fixed CSphMatchVariant::ToDocid conversion to match plain index behavior (fixes test 047 --rt)

*   fixed duplicates handling vs RT INSERT (first row wins now, not the last one)

*   added fetched_* counters collection to rt (fixes test_209 in --rt mode)

*   fixed keyword expansion in rt with docinfo=inline (fixes test_126 in --rt mode)

*   unified CSphIndex::SetupQueryTokenizer and sphSetupQueryTokenizer implementations, fixes most (but not all) of test 165 --rt

*   fixed off-by-1 in non-stemmed stopword check; fixed that lemmas got stemmed; fixed that wordforms could get applied twice through exact_dict; and rebuilt test 207 accordingly

*   improved RT insert speed (%7 gain in my batch insert test case)

*   indextool needs to preread checkpoints and infixes too

*   fixed mlock option on caching index files

*   fixed #2223 query cache last entry eviction during search cause daemon to hung

*   Expr_Rand_c speedup and fixes, thread-safe XorShift64, updated test 125

*   fixed #2053 added RAND() function

*   fixed #2230 memory corruption at daemon on inserting data into RT with bad HTML markup added regression to tests

*   fixed span length and lcs calculation in proximity queries

*   fixed performance on reading a lot of small buffers

*   fixed #2223 crash at watchdog shutdown on some OSes like centos, rhel

*   optimize RT inserts

*   refactoring

*   improving insertion speed into RT index (5% gain in my test)

*   refactoring, removed unneeded code

*   added RELOAD INDEX to SphinxQL

*   fixed #2209 prohibited order by MVA, added error message

*   fixed undefined reference to void ISphOutputBuffer::SendT in release version

*   new qcache defaults

*   lets handle 32bit weights in qcache

*   fixed a couple of memory leaks

*   fixed typo in vs2008 proj; added lost files to codeblocks projects

*   searchd.cpp splitted

*   fixed agent dashboard setup due to remove of workers

*   added test_232, positions coming out of the matching engine

*   fixed several bugs in qcache (bug #2191 and some more)

*   use RAII on CSphMutex instead of separate initialization method, fixed clang warnings

*   added feature #2195 memory mapping of all index files with separated caching thread daemon (re)start should be immediately and fix of &#039;old&#039; ondisk* issue fixed update of attributes for indexes with ondisk* option got rig and prohibit 32bit to 64bit index conversion on load got rid of all shared memory code

*   fixes in variant_match model generation (more compatible attr types, and better diff report)

*   fixed HTML stripper handling of broken PI (processing instruction) tags

*   added #2179 SphinxQL client timeout searchd section option sphinxql_timeout, default value is 900 seconds