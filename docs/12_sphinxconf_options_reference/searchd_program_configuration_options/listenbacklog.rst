listen\_backlog
~~~~~~~~~~~~~~~

TCP listen backlog. Optional, default is 5.

Windows builds currently (as of 0.9.9) can only process the requests one
by one. Concurrent requests will be enqueued by the TCP stack on OS
level, and requests that can not be enqueued will immediately fail with
“connection refused” message. listen\_backlog directive controls the
length of the connection queue. Non-Windows builds should work fine with
the default value.

Example:
^^^^^^^^

::


    listen_backlog = 20

