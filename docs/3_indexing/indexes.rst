Indexes
=======================

To be able to answer full-text search queries fast, Manticore needs to
build a special data structure optimized for such queries from your text
data. This structure is called *index*; and the process of building
index from text is called *indexing*.

Different index types are well suited for different tasks. For example,
a disk-based tree-based index would be easy to update (ie. insert new
documents to existing index), but rather slow to search. Manticore
architecture allows internally for different *index types*, or
*backends*, to be implemented comparatively easily.

Manticore provides 2 different backends: a <b>disk index</b> backend, and a
<b>RT (realtime) index</b> backend.

<b>Disk indexes</b> are designed to provide maximum indexing and
searching speed, while keeping the RAM footprint as low as possible.
That comes at a cost of text index updates. You can not update an
existing document or incrementally add a new document to a disk index.
You only can batch rebuild the entire disk index from scratch. (Note
that you still can update document's <b>attributes</b> on the fly, even
with the disk indexes.)

This “rebuild only” limitation might look as a big constraint at a first
glance. But in reality, it can very frequently be worked around rather
easily by setting up multiple disk indexes, searching through them all,
and only rebuilding the one with a fraction of the most recently changed
data. See `the section called “Live index
updates” <../live_index_updates.md>`__ for details.

<b>RT indexes</b> enable you to implement dynamic updates and
incremental additions to the full text index. RT stands for Real Time
and they are indeed “soft realtime” in terms of writes, meaning that
most index changes become available for searching as quick as 1
millisecond or less, but could occasionally stall for seconds. (Searches
will still work even during that occasional writing stall.) Refer to
`Chapter 4, *Real-time indexes* <../4_real-time_indexes/README.md>`__
for details.

Last but not least, Manticore supports so-called <b>distributed
indexes</b>. Compared to disk and RT indexes, those are not a real
physical backend, but rather just lists of either local or remote
indexes that can be searched transparently to the application, with
Manticore doing all the chores of sending search requests to remote
machines in the cluster, aggregating the result sets, retrying the
failed requests, and even doing some load balancing. See `the section
called “Distributed searching” <../distributed_searching.md>`__ for a
discussion of distributed indexes.

There can be as many indexes per configuration file as necessary.
``indexer`` utility can reindex either all of them (if ``--all`` option
is specified), or a certain explicitly specified subset. ``searchd``
utility will serve all the specified indexes, and the clients can
specify what indexes to search in run time.
