log
~~~

Log file name. Optional, default is ‘searchd.log’. All ``searchd`` run
time events will be logged in this file.

Also you can use the ‘syslog’ as the file name. In this case the events
will be sent to syslog daemon. To use the syslog option the sphinx must
be configured ‘–with-syslog’ on building.

Example:
^^^^^^^^

::


    log = /var/log/searchd.log

