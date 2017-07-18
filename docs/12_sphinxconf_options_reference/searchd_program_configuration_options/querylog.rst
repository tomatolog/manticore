query\_log
~~~~~~~~~~

Query log file name. Optional, default is empty (do not log queries).
All search queries will be logged in this file. The format is described
in `the section called “``searchd`` query log
formats” <../../searchd_query_log_formats/README.html>`__.

In case of ‘plain’ format, you can use the ‘syslog’ as the path to the
log file. In this case all search queries will be sent to syslog daemon
with LOG\_INFO priority, prefixed with ‘[query]’ instead of timestamp.
To use the syslog option the sphinx must be configured ‘–with-syslog’ on
building.

Example:
^^^^^^^^

::


    query_log = /var/log/query.log

