### binlog_max_log_size {#binlog-max-log-size}

Maximum binary log file size. Optional, default is 0 (do not reopen binlog file based on size). Introduced in version 1.10-beta.

A new binlog file will be forcibly opened once the current binlog file reaches this limit. This achieves a finer granularity of logs and can yield more efficient binlog disk usage under certain borderline workloads.

#### Example: {#example}

```

binlog_max_log_size = 16M

```