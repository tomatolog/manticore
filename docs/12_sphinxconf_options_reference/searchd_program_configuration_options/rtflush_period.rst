rt\_flush\_period
~~~~~~~~~~~~~~~~~

RT indexes RAM chunk flush check period, in seconds. Optional, default
is 10 hours. Introduced in version 2.0.1-beta.

Actively updated RT indexes that however fully fit in RAM chunks can
result in ever-growing binlogs, impacting disk use and crash recovery
time. With this directive the search daemon performs periodic flush
checks, and eligible RAM chunks can get saved, enabling consequential
binlog cleanup. See `the section called “Binary
logging” <../../binary_logging.rst>`__ for more details.

Example:
^^^^^^^^

::


    rt_flush_period = 3600 # 1 hour

