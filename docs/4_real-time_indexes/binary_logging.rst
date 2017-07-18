Binary logging
--------------

Binary logs are essentially a recovery mechanism. With binary logs
enabled, ``searchd`` writes every given transaction to the binlog file,
and uses that for recovery after an unclean shutdown. On clean shutdown,
RAM chunks are saved to disk, and then all the binlog files are
unlinked.

During normal operation, a new binlog file will be opened every time
when ``binlog_max_log_size`` limit is reached. Older, already closed
binlog files are kept until all of the transactions stored in them (from
all indexes) are flushed as a disk chunk. Setting the limit to 0 pretty
much prevents binlog from being unlinked at all while ``searchd`` is
running; however, it will still be unlinked on clean shutdown. (This is
the default case as of 2.0.3-release, ``binlog_max_log_size`` defaults
to 0.)

There are 3 different binlog flushing strategies, controlled by
`binlog\_flush <../searchd_program_configuration_options/binlogflush.html>`__
directive which takes the values of 0, 1, or 2. 0 means to flush the log
to OS and sync it to disk every second; 1 means flush and sync every
transaction; and 2 (the default mode) means flush every transaction but
sync every second. Sync is relatively slow because it has to perform
physical disk writes, so mode 1 is the safest (every committed
transaction is guaranteed to be written on disk) but the slowest.
Flushing log to OS prevents from data loss on ``searchd`` crashes but
not system crashes. Mode 2 is the default.

On recovery after an unclean shutdown, binlogs are replayed and all
logged transactions since the last good on-disk state are restored.
Transactions are checksummed so in case of binlog file corruption
garbage data will <b>not</b> be replayed; such a broken transaction will
be detected and, currently, will stop replay. Transactions also start
with a magic marker and timestamped, so in case of binlog damage in the
middle of the file, it's technically possible to skip broken
transactions and keep replaying from the next good one, and/or it's
possible to replay transactions until a given timestamp (point-in-time
recovery), but none of that is implemented yet as of 1.10-beta.

One unwanted side effect of binlogs is that actively updating a small RT
index that fully fits into a RAM chunk part will lead to an ever-growing
binlog that can never be unlinked until clean shutdown. Binlogs are
essentially append-only deltas against the last known good saved state
on disk, and unless RAM chunk gets saved, they can not be unlinked. An
ever-growing binlog is not very good for disk use and crash recovery
time. Starting with 2.0.1-beta you can configure ``searchd`` to perform
a periodic RAM chunk flush to fix that problem using a
`rt\_flush\_period <../searchd_program_configuration_options/rtflush_period.html>`__
directive. With periodic flushes enabled, ``searchd`` will keep a
separate thread, checking whether RT indexes RAM chunks need to be
written back to disk. Once that happens, the respective binlogs can be
(and are) safely unlinked.

Note that ``rt_flush_period`` only controls the frequency at which the
*checks* happen. There are no *guarantees* that the particular RAM chunk
will get saved. For instance, it does not make sense to regularly
re-save a huge RAM chunk that only gets a few rows worth of updates. The
search daemon determine whether to actually perform the flush with a few
heuristics.
