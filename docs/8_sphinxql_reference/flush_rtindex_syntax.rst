FLUSH RTINDEX syntax
--------------------

::


    FLUSH RTINDEX rtindex

FLUSH RTINDEX statement, added in version 2.0.2-beta, forcibly flushes
RT index RAM chunk contents to disk.

Backing up a RT index is as simple as copying over its data files,
followed by the binary log. However, recovering from that backup means
that all the transactions in the log since the last successful RAM chunk
write would need to be replayed. Those writes normally happen either on
a clean shutdown, or periodically with a (big enough!) interval between
writes specified in
`rt\_flush\_period <../searchd_program_configuration_options/rtflush_period.rst>`__
directive. So such a backup made at an arbitrary point in time just
might end up with way too much binary log data to replay.

FLUSH RTINDEX forcibly writes the RAM chunk contents to disk, and also
causes the subsequent cleanup of (now-redundant) binary log files. Thus,
recovering from a backup made just after FLUSH RTINDEX should be almost
instant.

::


    mysql> FLUSH RTINDEX rt;
    Query OK, 0 rows affected (0.05 sec)

