SHOW PROFILE syntax
-------------------

::


    SHOW PROFILE

SHOW PROFILE shows a detailed execution profile of the previous SQL
statement executed in the current SphinxQL session. Also, profiling must
be enabled in the current session <b>before</b> running the statement to
be instrumented. That can be done with a ``SET profiling=1`` statement.
By default, profiling is disabled to avoid potential performance
implications, and therefore the profile will be empty.

Here's a complete instrumentation example:

::


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

Status column briefly describes where exactly (in which state) was the
time spent. Duration column shows the wall clock time, in seconds.
Switches column displays the number of times query engine changed to the
given state. Those are just logical engine state switches and <b>not</b>
any OS level context switches nor function calls (even though some of
the sections can actually map to function calls) and they do <b>not</b>
have any direct effect on the performance. In a sense, number of
switches is just a number of times when the respective instrumentation
point was hit.

States in the profile are returned in a prerecorded order that roughly
maps (but is <b>not</b> identical) to the actual query order.

A list of states may (and will) vary over time, as we refine the states.
Here's a brief description of the currently profiled states.

-  <b>unknown</b>, generic catch-all state. Accounts for both
   not-yet-instrumented code, or just small miscellaneous tasks that do
   not really belong in any other state, but are too small to deserve
   their own state.
-  <b>net\_read</b>, reading the query from the network (that is, the
   application).
-  <b>io</b>, generic file IO time.
-  <b>dist\_connect</b>, connecting to remote agents in the distributed
   index case.
-  <b>sql\_parse</b>, parsing the SphinxQL syntax.
-  <b>dict\_setup</b>, dictionary and tokenizer setup.
-  <b>parse</b>, parsing the full-text query syntax.
-  <b>transforms</b>, full-text query transformations (wildcard and
   other expansions, simplification, etc).
-  <b>init</b>, initializing the query evaluation.
-  <b>open</b>, opening the index files.
-  <b>read\_docs</b>, IO time spent reading document lists.
-  <b>read\_hits</b>, IO time spent reading keyword positions.
-  <b>get\_docs</b>, computing the matching documents.
-  <b>get\_hits</b>, computing the matching positions.
-  <b>filter</b>, filtering the full-text matches.
-  <b>rank</b>, computing the relevance rank.
-  <b>sort</b>, sorting the matches.
-  <b>finalize</b>, finalizing the per-index search result set (last
   stage expressions, etc).
-  <b>dist\_wait</b>, waiting for the remote results from the agents in
   the distributed index case.
-  <b>aggregate</b>, aggregating multiple result sets.
-  <b>net\_write</b>, writing the result set to the network.
