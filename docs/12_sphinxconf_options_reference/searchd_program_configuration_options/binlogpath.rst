binlog\_path
~~~~~~~~~~~~

Binary log (aka transaction log) files path. Optional, default is
build-time configured data directory.

Binary logs are used for crash recovery of RT index data, and also of
attributes updates of plain disk indices that would otherwise only be
stored in RAM until flush. When logging is enabled, every transaction
COMMIT-ted into RT index gets written into a log file. Logs are then
automatically replayed on startup after an unclean shutdown, recovering
the logged changes.

``binlog_path`` directive specifies the binary log files location. It
should contain just the path; ``searchd`` will create and unlink
multiple binlog.\* files in that path as necessary (binlog data,
metadata, and lock files, etc).

Empty value disables binary logging. That improves performance, but puts
RT index data at risk.

WARNING! It is strongly recommended to always explicitly define
‘binlog\_path’ option in your config. Otherwise, the default path, which
in most cases is the same as working folder, may point to the folder
with no write access (for example, /usr/local/var/data). In this case,
the searchd will not start at all.

Example:
^^^^^^^^

::


    binlog_path = # disable logging
    binlog_path = /var/data # /var/data/binlog.001 etc will be created

