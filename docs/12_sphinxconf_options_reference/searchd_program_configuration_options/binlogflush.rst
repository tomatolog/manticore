binlog\_flush
~~~~~~~~~~~~~

Binary log transaction flush/sync mode. Optional, default is 2 (flush
every transaction, sync every second). Introduced in version 1.10-beta.

This directive controls how frequently will binary log be flushed to OS
and synced to disk. Three modes are supported:

-  0, flush and sync every second. Best performance, but up to 1 second
   worth of committed transactions can be lost both on daemon crash, or
   OS/hardware crash.

-  1, flush and sync every transaction. W.html performance, but every
   committed transaction data is guaranteed to be saved.

-  2, flush every transaction, sync every second. Good performance, and
   every committed transaction is guaranteed to be saved in case of
   daemon crash. However, in case of OS/hardware crash up to 1 second
   worth of committed transactions can be lost.

For those familiar with MySQL and InnoDB, this directive is entirely
similar to ``innodb_flush_log_at_trx_commit``. In most cases, the
default hybrid mode 2 provides a nice balance of speed and safety, with
full RT index data protection against daemon crashes, and some
protection against hardware ones.

Example:
^^^^^^^^

::


    binlog_flush = 1 # ultimate safety, low speed

