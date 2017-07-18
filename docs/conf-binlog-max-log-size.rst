.. raw:: html

   <div class="navheader">

12.4.30. binlog\_max\_log\_size
`Prev <conf-binlog-flush.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-snippets-file-prefix.html>`__

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

.. rubric:: 12.4.30. binlog\_max\_log\_size
   :name: binlog_max_log_size
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Maximum binary log file size. Optional, default is 0 (do not reopen
binlog file based on size). Introduced in version 1.10-beta.

A new binlog file will be forcibly opened once the current binlog file
reaches this limit. This achieves a finer granularity of logs and can
yield more efficient binlog disk usage under certain borderline
workloads.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    binlog_max_log_size = 16M

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------+-----------------------------------+----------------------------------------------+
| `Prev <conf-binlog-flush.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-snippets-file-prefix.html>`__   |
+--------------------------------------+-----------------------------------+----------------------------------------------+
| 12.4.29. binlog\_flush               | `Home <index.html>`__             |  12.4.31. snippets\_file\_prefix             |
+--------------------------------------+-----------------------------------+----------------------------------------------+

.. raw:: html

   </div>
