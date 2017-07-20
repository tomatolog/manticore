shutdown\_timeout
~~~~~~~~~~~~~~~~~

searchd –stopwait wait time, in seconds. Optional, default is 3 seconds.

When you run searchd –stopwait your daemon needs to perform some
activities before stopping like finishing queries, flushing RT RAM
chunk, flushing attributes and updating binlog. And it requires some
time. searchd –stopwait will wait up to shutdown\_time seconds for
daemon to finish its jobs. Suitable time depends on your index size and
load.

Example:
^^^^^^^^

::


    shutdown_timeout = 5 # wait for up to 5 seconds

