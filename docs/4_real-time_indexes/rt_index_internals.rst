RT index internals
------------------

RT index is internally chunked. It keeps a so-called RAM chunk that
stores all the most recent changes. RAM chunk memory usage is rather
strictly limited with per-index
`rt\_mem\_limit <../index_configuration_options/rtmem_limit.md>`__
directive. Once RAM chunk grows over this limit, a new disk chunk is
created from its data, and RAM chunk is reset. Thus, while most changes
on the RT index will be performed in RAM only and complete instantly (in
milliseconds), those changes that overflow the RAM chunk will stall for
the duration of disk chunk creation (a few seconds).

Since version 2.1.1-beta, Sphinx uses double-buffering to avoid INSERT
stalls. When data is being dumped to disk, the second buffer is used, so
further INSERTs won't be delayed. The second buffer is defined to be 10%
the size of the standard buffer,
`rt\_mem\_limit <../index_configuration_options/rtmem_limit.md>`__, but
future versions of Sphinx may allow configuring this further.

Disk chunks are, in fact, just regular disk-based indexes. But they're a
part of an RT index and automatically managed by it, so you need not
configure nor manage them manually. Because a new disk chunk is created
every time RT chunk overflows the limit, and because in-memory chunk
format is close to on-disk format, the disk chunks will be approximately
``rt_mem_limit`` bytes in size each.

Generally, it is better to set the limit bigger, to minimize both the
frequency of flushes, and the index fragmentation (number of disk
chunks). For instance, on a dedicated search server that handles a big
RT index, it can be advised to set ``rt_mem_limit`` to 1-2 GB. A global
limit on all indexes is also planned, but not yet implemented yet as of
1.10-beta.

Disk chunk full-text index data can not be actually modified, so the
full-text field changes (ie. row deletions and updates) suppress a
previous row version from a disk chunk using a kill-list, but do not
actually physically purge the data. Therefore, on workloads with high
full-text updates ratio index might eventually get polluted by these
previous row versions, and searching performance would degrade. Physical
index purging that would improve the performance is planned, but not yet
implemented as of 1.10-beta.

Data in RAM chunk gets saved to disk on clean daemon shutdown, and then
loaded back on startup. However, on daemon or server crash, updates from
RAM chunk might be lost. To prevent that, binary logging of transactions
can be used; see `the section called “Binary
logging” <../binary_logging.md>`__ for details.

Full-text changes in RT index are transactional. They are stored in a
per-thread accumulator until COMMIT, then applied at once. Bigger
batches per single COMMIT should result in faster indexing.
