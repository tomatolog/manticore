dist\_threads
~~~~~~~~~~~~~

Max local worker threads to use for parallelizable requests (searching a
distributed index; building a batch of snippets). Optional, default is
0, which means to disable in-request parallelism. Introduced in version
1.10-beta.

Distributed index can include several local indexes. ``dist_threads``
lets you easily utilize multiple CPUs/cores for that (previously
existing alternative was to specify the indexes as remote agents,
pointing searchd to itself and paying some network overheads).

When set to a value N greater than 1, this directive will create up to N
threads for every query, and schedule the specific searches within these
threads. For example, if there are 7 local indexes to search and
dist\_threads is set to 2, then 2 parallel threads would be created: one
that sequentially searches 4 indexes, and another one that searches the
other 3 indexes.

In case of CPU bound workload, setting ``dist_threads`` to 1x the number
of cores is advised (creating more threads than cores will not improve
query time). In case of mixed CPU/disk bound workload it might sometimes
make sense to use more (so that all cores could be utilizes even when
there are threads that wait for I/O completion).

Starting with version 2.0.1-beta, building a batch of snippets with
``load_files`` flag enabled can also be parallelized. Up to
``dist_threads`` threads are be created to process those files. That
speeds up snippet extraction when the total amount of document data to
process is significant (hundreds of megabytes).

Example:
^^^^^^^^

::


    index dist_test
    {
        type = distributed
        local = chunk1
        local = chunk2
        local = chunk3
        local = chunk4
    }

    # ...

    dist_threads = 4

