### log {#log}

Log file name. Optional, default is &#039;searchd.log&#039;. All `searchd` run time events will be logged in this file.

Also you can use the &#039;syslog&#039; as the file name. In this case the events will be sent to syslog daemon. To use the syslog option the sphinx must be configured &#039;--with-syslog&#039; on building.

#### Example: {#example}

```

log = /var/log/searchd.log

```