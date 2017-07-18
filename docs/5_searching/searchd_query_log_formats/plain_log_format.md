### Plain log format {#plain-log-format}

By default, `searchd` logs all successfully executed search queries into a query log file. Here&#039;s an example:

```

[Fri Jun 29 21:17:58 2007] 0.004 sec 0.004 sec [all/0/rel 35254 (0,20)] [lj] test
[Fri Jun 29 21:20:34 2007] 0.024 sec 0.024 sec [all/0/rel 19886 (0,20) @channel_id] [lj] test

```

This log format is as follows:

```

[query-date] real-time wall-time [match-mode/filters-count/sort-mode
    total-matches (offset,limit) @groupby-attr] [index-name] query

```

*   real-time is a time measured just from start to finish of the query

*   wall-time like real-time but not including waiting for agents and merging result sets time

Match mode can take one of the following values:

*   &quot;all&quot; for SPH_MATCH_ALL mode;

*   &quot;any&quot; for SPH_MATCH_ANY mode;

*   &quot;phr&quot; for SPH_MATCH_PHRASE mode;

*   &quot;bool&quot; for SPH_MATCH_BOOLEAN mode;

*   &quot;ext&quot; for SPH_MATCH_EXTENDED mode;

*   &quot;ext2&quot; for SPH_MATCH_EXTENDED2 mode;

*   &quot;scan&quot; if the full scan mode was used, either by being specified with SPH_MATCH_FULLSCAN, or if the query was empty (as documented under [Matching Modes](../../matching_modes.md))

Sort mode can take one of the following values:

*   &quot;rel&quot; for SPH_SORT_RELEVANCE mode;

*   &quot;attr-&quot; for SPH_SORT_ATTR_DESC mode;

*   &quot;attr+&quot; for SPH_SORT_ATTR_ASC mode;

*   &quot;tsegs&quot; for SPH_SORT_TIME_SEGMENTS mode;

*   &quot;ext&quot; for SPH_SORT_EXTENDED mode.

Additionally, if `searchd` was started with `--iostats`, there will be a block of data after where the index(es) searched are listed.

A query log entry might take the form of:

```

[Fri Jun 29 21:17:58 2007] 0.004 sec [all/0/rel 35254 (0,20)] [lj]
   [ios=6 kb=111.1 ms=0.5] test

```

This additional block is information regarding I/O operations in performing the search: the number of file I/O operations carried out, the amount of data in kilobytes read from the index files and time spent on I/O operations (although there is a background processing component, the bulk of this time is the I/O operation time).