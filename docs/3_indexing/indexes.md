## Indexes {#indexes}

To be able to answer full-text search queries fast, Sphinx needs to build a special data structure optimized for such queries from your text data. This structure is called _index_; and the process of building index from text is called _indexing_.

Different index types are well suited for different tasks. For example, a disk-based tree-based index would be easy to update (ie. insert new documents to existing index), but rather slow to search. Sphinx architecture allows internally for different _index types_, or _backends_, to be implemented comparatively easily.

Starting with 1.10-beta, Sphinx provides 2 different backends: a &lt;b&gt;disk index&lt;/b&gt; backend, and a &lt;b&gt;RT (realtime) index&lt;/b&gt; backend.

&lt;b&gt;Disk indexes&lt;/b&gt; are designed to provide maximum indexing and searching speed, while keeping the RAM footprint as low as possible. That comes at a cost of text index updates. You can not update an existing document or incrementally add a new document to a disk index. You only can batch rebuild the entire disk index from scratch. (Note that you still can update document&#039;s &lt;b&gt;attributes&lt;/b&gt; on the fly, even with the disk indexes.)

This &quot;rebuild only&quot; limitation might look as a big constraint at a first glance. But in reality, it can very frequently be worked around rather easily by setting up multiple disk indexes, searching through them all, and only rebuilding the one with a fraction of the most recently changed data. See [the section called “Live index updates”](../live_index_updates.md) for details.

&lt;b&gt;RT indexes&lt;/b&gt; enable you to implement dynamic updates and incremental additions to the full text index. RT stands for Real Time and they are indeed &quot;soft realtime&quot; in terms of writes, meaning that most index changes become available for searching as quick as 1 millisecond or less, but could occasionally stall for seconds. (Searches will still work even during that occasional writing stall.) Refer to [Chapter 4, _Real-time indexes_](../4_real-time_indexes/README.md) for details.

Last but not least, Sphinx supports so-called &lt;b&gt;distributed indexes&lt;/b&gt;. Compared to disk and RT indexes, those are not a real physical backend, but rather just lists of either local or remote indexes that can be searched transparently to the application, with Sphinx doing all the chores of sending search requests to remote machines in the cluster, aggregating the result sets, retrying the failed requests, and even doing some load balancing. See [the section called “Distributed searching”](../distributed_searching.md) for a discussion of distributed indexes.

There can be as many indexes per configuration file as necessary. `indexer` utility can reindex either all of them (if `--all` option is specified), or a certain explicitly specified subset. `searchd` utility will serve all the specified indexes, and the clients can specify what indexes to search in run time.