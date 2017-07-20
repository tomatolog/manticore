local
~~~~~

Local index declaration in the `distributed
index <../../distributed_searching.md>`__. Multi-value, optional,
default is empty.

This setting is used to declare local indexes that will be searched when
given distributed index is searched. Many local indexes can be declared
per each distributed index. Any local index can also be mentioned
several times in different distributed indexes.

Note that by default all local indexes will be searched
<b>sequentially</b>, utilizing only 1 CPU or core. To parallelize
processing of the local parts in the distributed index, you should use
``dist_threads`` directive, see `the section called
“dist\_threads” <../../searchd_program_configuration_options/distthreads.md>`__.

Before ``dist_threads``, there also was a legacy solution to configure
``searchd`` to query itself instead of using local indexes (refer to
`the section called
“agent” <../../index_configuration_options/agent.md>`__ for the
details). However, that creates redundant CPU and network load, and
``dist_threads`` is now strongly suggested instead.

Example:
^^^^^^^^

::


    local = chunk1
    local = chunk2

