rt\_merge\_iops
~~~~~~~~~~~~~~~

A maximum number of I/O operations (per second) that the RT chunks merge
thread is allowed to start. Optional, default is 0 (no limit). Added in
2.1.1-beta.

This directive lets you throttle down the I/O impact arising from the
``OPTIMIZE`` statements. It is guaranteed that all the RT optimization
activity will not generate more disk iops (I/Os per second) than the
configured limit. Modern SATA drives can perform up to around 100 I/O
operations per second, and limiting rt\_merge\_iops can reduce search
performance degradation caused by merging.

Example:
^^^^^^^^

::


    rt_merge_iops = 40

