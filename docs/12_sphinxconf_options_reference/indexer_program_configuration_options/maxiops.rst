max\_iops
~~~~~~~~~

Maximum I/O operations per second, for I/O throttling. Optional, default
is 0 (unlimited).

I/O throttling related option. It limits maximum count of I/O operations
(reads or writes) per any given second. A value of 0 means that no limit
is imposed.

``indexer`` can cause b.htmls of intensive disk I/O during indexing, and
it might desired to limit its disk activity (and keep something for
other programs running on the same machine, such as ``searchd``). I/O
throttling helps to do that. It works by enforcing a minimum guaranteed
delay between subsequent disk I/O operations performed by ``indexer``.
Modern SATA HDDs are able to perform up to 70-100+ I/O operations per
second (that's mostly limited by disk heads seek time). Limiting
indexing I/O to a fraction of that can help reduce search performance
degradation caused by indexing.

Example:
^^^^^^^^

::


    max_iops = 40

