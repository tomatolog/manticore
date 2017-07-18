.. raw:: html

   <div class="navheader">

8.3. SHOW META syntax
`Prev <sphinxql-select-sysvar.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-show-warnings.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect1">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 8.3. SHOW META syntax
   :name: show-meta-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    SHOW META [ LIKE pattern ]

**SHOW META** shows additional meta-information about the latest query
such as query time and keyword statistics. IO and CPU counters will only
be available if searchd was started with –iostats and –cpustats switches
respectively. Additional predicted\_time, dist\_predicted\_time,
[{local\|dist}]\_fetched\_[{docs\|hits\|skips}] counters will only be
available if searchd was configured with `predicted time
costs <conf-predicted-time-costs.html>`__ and query had predicted\_time
in OPTION clause.

.. code:: programlisting

    mysql> SELECT * FROM test1 WHERE MATCH('test|one|two');
    +------+--------+----------+------------+
    | id   | weight | group_id | date_added |
    +------+--------+----------+------------+
    |    1 |   3563 |      456 | 1231721236 |
    |    2 |   2563 |      123 | 1231721236 |
    |    4 |   1480 |        2 | 1231721236 |
    +------+--------+----------+------------+
    3 rows in set (0.01 sec)

    mysql> SHOW META;
    +-----------------------+-------+
    | Variable_name         | Value |
    +-----------------------+-------+
    | total                 | 3     |
    | total_found           | 3     |
    | time                  | 0.005 |
    | keyword[0]            | test  |
    | docs[0]               | 3     |
    | hits[0]               | 5     |
    | keyword[1]            | one   |
    | docs[1]               | 1     |
    | hits[1]               | 2     |
    | keyword[2]            | two   |
    | docs[2]               | 1     |
    | hits[2]               | 2     |
    | cpu_time              | 0.350 |
    | io_read_time          | 0.004 |
    | io_read_ops           | 2     |
    | io_read_kbytes        | 0.4   |
    | io_write_time         | 0.000 |
    | io_write_ops          | 0     |
    | io_write_kbytes       | 0.0   |
    | agents_cpu_time       | 0.000 |
    | agent_io_read_time    | 0.000 |
    | agent_io_read_ops     | 0     |
    | agent_io_read_kbytes  | 0.0   |
    | agent_io_write_time   | 0.000 |
    | agent_io_write_ops    | 0     |
    | agent_io_write_kbytes | 0.0   |
    +-----------------------+-------+
    12 rows in set (0.00 sec)

Starting version 2.1.1-beta, you can also use the optional LIKE clause.
It lets you pick just the variables that match a pattern. The pattern
syntax is that of regular SQL wildcards, that is, ‘%’ means any number
of any characters, and ‘\_’ means a single character:

.. code:: programlisting

    mysql> SHOW META LIKE 'total%';
    +-----------------------+-------+
    | Variable_name         | Value |
    +-----------------------+-------+
    | total                 | 3     |
    | total_found           | 3     |
    +-----------------------+-------+
    2 rows in set (0.00 sec)

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+------------------------------------+-------------------------------------------+
| `Prev <sphinxql-select-sysvar.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-show-warnings.html>`__   |
+-------------------------------------------+------------------------------------+-------------------------------------------+
| 8.2. SELECT @@system\_variable syntax     | `Home <index.html>`__              |  8.4. SHOW WARNINGS syntax                |
+-------------------------------------------+------------------------------------+-------------------------------------------+

.. raw:: html

   </div>
