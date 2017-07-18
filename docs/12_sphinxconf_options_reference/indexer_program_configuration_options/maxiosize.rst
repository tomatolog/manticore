max\_iosize
~~~~~~~~~~~

Maximum allowed I/O operation size, in bytes, for I/O throttling.
Optional, default is 0 (unlimited).

I/O throttling related option. It limits maximum file I/O operation
(read or write) size for all operations performed by ``indexer``. A
value of 0 means that no limit is imposed. Reads or writes that are
bigger than the limit will be split in several smaller operations, and
counted as several operation by
`max\_iops <../../indexer_program_configuration_options/maxiops.rst>`__
setting. At the time of this writing, all I/O calls should be under 256
KB (default internal buffer size) anyway, so ``max_iosize`` values
higher than 256 KB must not affect anything.

Example:
^^^^^^^^

::


    max_iosize = 1048576

