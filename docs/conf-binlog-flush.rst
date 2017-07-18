.. raw:: html

   <div class="navheader">

12.4.29. binlog\_flush
`Prev <conf-binlog-path.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-binlog-max-log-size.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect2">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 12.4.29. binlog\_flush
   :name: binlog_flush
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Binary log transaction flush/sync mode. Optional, default is 2 (flush
every transaction, sync every second). Introduced in version 1.10-beta.

This directive controls how frequently will binary log be flushed to OS
and synced to disk. Three modes are supported:

.. raw:: html

   <div class="itemizedlist">

-  0, flush and sync every second. Best performance, but up to 1 second
   worth of committed transactions can be lost both on daemon crash, or
   OS/hardware crash.

-  1, flush and sync every transaction. Worst performance, but every
   committed transaction data is guaranteed to be saved.

-  2, flush every transaction, sync every second. Good performance, and
   every committed transaction is guaranteed to be saved in case of
   daemon crash. However, in case of OS/hardware crash up to 1 second
   worth of committed transactions can be lost.

.. raw:: html

   </div>

For those familiar with MySQL and InnoDB, this directive is entirely
similar to ``innodb_flush_log_at_trx_commit``. In most cases, the
default hybrid mode 2 provides a nice balance of speed and safety, with
full RT index data protection against daemon crashes, and some
protection against hardware ones.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    binlog_flush = 1 # ultimate safety, low speed

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------+-----------------------------------+---------------------------------------------+
| `Prev <conf-binlog-path.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-binlog-max-log-size.html>`__   |
+-------------------------------------+-----------------------------------+---------------------------------------------+
| 12.4.28. binlog\_path               | `Home <index.html>`__             |  12.4.30. binlog\_max\_log\_size            |
+-------------------------------------+-----------------------------------+---------------------------------------------+

.. raw:: html

   </div>
