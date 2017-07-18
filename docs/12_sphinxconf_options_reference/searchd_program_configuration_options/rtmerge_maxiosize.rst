rt\_merge\_maxiosize
~~~~~~~~~~~~~~~~~~~~

A maximum size of an I/O operation that the RT chunks merge thread is
allowed to start. Optional, default is 0 (no limit). Added in
2.1.1-beta.

This directive lets you throttle down the I/O impact arising from the
``OPTIMIZE`` statements. I/Os bigger than this limit will be broken down
into 2 or more I/Os, which will then be accounted as separate I/Os with
regards to the
`rt\_merge\_iops <../../searchd_program_configuration_options/rtmerge_iops.rst>`__
limit. Thus, it is guaranteed that all the optimization activity will
not generate more than (rt\_merge\_iops \* rt\_merge\_maxiosize) bytes
of disk I/O per second.

Example:
^^^^^^^^

::


    rt_merge_maxiosize = 1M

