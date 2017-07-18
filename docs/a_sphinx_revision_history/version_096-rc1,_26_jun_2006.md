## Version 0.9.6-rc1, 26 jun 2006 {#version-0-9-6-rc1-26-jun-2006}

*   added boolean queries support (experimental, beta version)

*   added simple file-based query cache (experimental, beta version)

*   added storage engine for MySQL 5.0 and 5.1 (experimental, beta version)

*   added GNU style `configure` script

*   added new searchd protocol (all binary, and should be backwards compatible)

*   added distributed searching support to searchd

*   added PostgreSQL driver

*   added excerpts generation

*   added `min_word_len` option to index

*   added `max_matches` option to searchd, removed hardcoded MAX_MATCHES limit

*   added initial documentation, and a working `example.sql`

*   added support for multiple sources per index

*   added soundex support

*   added group ID ranges support

*   added `--stdin` command-line option to search utility

*   added `--noprogress` option to indexer

*   added `--index` option to search

*   fixed UTF-8 decoder (3-byte codepoints did not work)

*   fixed PHP API to handle big result sets faster

*   fixed config parser to handle empty values properly

*   fixed redundant `time(NULL)` calls in time-segments mode