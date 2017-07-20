Live index updates
------------------

There are two major approaches to maintaining the full-text index
contents up to date. Note, however, that both these approaches deal with
the task of *full-text data updates*, and not attribute updates (which
are already supported, refer to
`UpdateAttributes() <../additional_functionality/updateattributes.md>`__
API call description for details.)

First, you can use disk-based indexes, partition them manually, and only
rebuild the smaller partitions (so-called “deltas”) frequently. By
minimizing the rebuild size, you can reduce the average indexing lag to
something as low as 30-60 seconds. On huge collections it actually might
be the most efficient one. Refer to `the section called “Delta index
updates” <../delta_index_updates.md>`__ for details.

Second, using real-time indexes (RT indexes for short) that on-the-fly
updates of the full-text data. Updates on a RT index can appear in the
search results in 1-2 milliseconds, ie. 0.001-0.002 seconds. However, RT
index are less efficient for bulk indexing huge amounts of data. Refer
to `Chapter 4, *Real-time indexes* <../4_real-time_indexes/README.md>`__
for details.
