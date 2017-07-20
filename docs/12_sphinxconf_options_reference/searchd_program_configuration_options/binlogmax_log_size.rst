binlog\_max\_log\_size
~~~~~~~~~~~~~~~~~~~~~~

Maximum binary log file size. Optional, default is 0 (do not reopen
binlog file based on size).

A new binlog file will be forcibly opened once the current binlog file
reaches this limit. This achieves a finer granularity of logs and can
yield more efficient binlog disk usage under certain borderline
workloads.

Example:
^^^^^^^^

::


    binlog_max_log_size = 16M

