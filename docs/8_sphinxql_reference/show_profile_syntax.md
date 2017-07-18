## SHOW PROFILE syntax {#show-profile-syntax}

```

SHOW PROFILE

```

SHOW PROFILE statement, added in version 2.1.1-beta, shows a detailed execution profile of the previous SQL statement executed in the current SphinxQL session. Also, profiling must be enabled in the current session &lt;b&gt;before&lt;/b&gt; running the statement to be instrumented. That can be done with a `SET profiling=1` statement. By default, profiling is disabled to avoid potential performance implications, and therefore the profile will be empty.

Here&#039;s a complete instrumentation example:

```

mysql> SET profiling=1;
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT id FROM lj WHERE MATCH('the test') LIMIT 1;
+--------+
| id     |
+--------+
| 946418 |
+--------+
1 row in set (0.05 sec)

mysql> SHOW PROFILE;
+--------------+----------+----------+
| Status       | Duration | Switches |
+--------------+----------+----------+
| unknown      | 0.000610 | 6        |
| net_read     | 0.000007 | 1        |
| dist_connect | 0.000036 | 1        |
| sql_parse    | 0.000048 | 1        |
| dict_setup   | 0.000001 | 1        |
| parse        | 0.000023 | 1        |
| transforms   | 0.000002 | 1        |
| init         | 0.000401 | 3        |
| open         | 0.000104 | 1        |
| read_docs    | 0.001570 | 71       |
| read_hits    | 0.003936 | 222      |
| get_docs     | 0.029837 | 1347     |
| get_hits     | 0.000548 | 1433     |
| filter       | 0.000619 | 1274     |
| rank         | 0.009892 | 2909     |
| sort         | 0.001562 | 52       |
| finalize     | 0.000250 | 1        |
| dist_wait    | 0.000000 | 1        |
| aggregate    | 0.000145 | 1        |
| net_write    | 0.000031 | 1        |
+--------------+----------+----------+
20 rows in set (0.00 sec)

```

Status column briefly describes where exactly (in which state) was the time spent. Duration column shows the wall clock time, in seconds. Switches column displays the number of times query engine changed to the given state. Those are just logical engine state switches and &lt;b&gt;not&lt;/b&gt; any OS level context switches nor function calls (even though some of the sections can actually map to function calls) and they do &lt;b&gt;not&lt;/b&gt; have any direct effect on the performance. In a sense, number of switches is just a number of times when the respective instrumentation point was hit.

States in the profile are returned in a prerecorded order that roughly maps (but is &lt;b&gt;not&lt;/b&gt; identical) to the actual query order.

A list of states may (and will) vary over time, as we refine the states. Here&#039;s a brief description of the currently profiled states.

*   &lt;b&gt;unknown&lt;/b&gt;, generic catch-all state. Accounts for both not-yet-instrumented code, or just small miscellaneous tasks that do not really belong in any other state, but are too small to deserve their own state.
*   &lt;b&gt;net_read&lt;/b&gt;, reading the query from the network (that is, the application).
*   &lt;b&gt;io&lt;/b&gt;, generic file IO time.
*   &lt;b&gt;dist_connect&lt;/b&gt;, connecting to remote agents in the distributed index case.
*   &lt;b&gt;sql_parse&lt;/b&gt;, parsing the SphinxQL syntax.
*   &lt;b&gt;dict_setup&lt;/b&gt;, dictionary and tokenizer setup.
*   &lt;b&gt;parse&lt;/b&gt;, parsing the full-text query syntax.
*   &lt;b&gt;transforms&lt;/b&gt;, full-text query transformations (wildcard and other expansions, simplification, etc).
*   &lt;b&gt;init&lt;/b&gt;, initializing the query evaluation.
*   &lt;b&gt;open&lt;/b&gt;, opening the index files.
*   &lt;b&gt;read_docs&lt;/b&gt;, IO time spent reading document lists.
*   &lt;b&gt;read_hits&lt;/b&gt;, IO time spent reading keyword positions.
*   &lt;b&gt;get_docs&lt;/b&gt;, computing the matching documents.
*   &lt;b&gt;get_hits&lt;/b&gt;, computing the matching positions.
*   &lt;b&gt;filter&lt;/b&gt;, filtering the full-text matches.
*   &lt;b&gt;rank&lt;/b&gt;, computing the relevance rank.
*   &lt;b&gt;sort&lt;/b&gt;, sorting the matches.
*   &lt;b&gt;finalize&lt;/b&gt;, finalizing the per-index search result set (last stage expressions, etc).
*   &lt;b&gt;dist_wait&lt;/b&gt;, waiting for the remote results from the agents in the distributed index case.
*   &lt;b&gt;aggregate&lt;/b&gt;, aggregating multiple result sets.
*   &lt;b&gt;net_write&lt;/b&gt;, writing the result set to the network.