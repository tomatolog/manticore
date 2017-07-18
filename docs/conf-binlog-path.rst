.. raw:: html

   <div class="navheader">

12.4.28. binlog\_path
`Prev <conf-dist-threads.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-binlog-flush.html>`__

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

.. rubric:: 12.4.28. binlog\_path
   :name: binlog_path
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Binary log (aka transaction log) files path. Optional, default is
build-time configured data directory. Introduced in version 1.10-beta.

Binary logs are used for crash recovery of RT index data, and also of
attributes updates of plain disk indices that would otherwise only be
stored in RAM until flush. When logging is enabled, every transaction
COMMIT-ted into RT index gets written into a log file. Logs are then
automatically replayed on startup after an unclean shutdown, recovering
the logged changes.

``binlog_path`` directive specifies the binary log files location. It
should contain just the path; ``searchd`` will create and unlink
multiple binlog.\* files in that path as necessary (binlog data,
metadata, and lock files, etc).

Empty value disables binary logging. That improves performance, but puts
RT index data at risk.

WARNING! It is strongly recommended to always explicitly define
‘binlog\_path’ option in your config. Otherwise, the default path, which
in most cases is the same as working folder, may point to the folder
with no write access (for example, /usr/local/var/data). In this case,
the searchd will not start at all.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    binlog_path = # disable logging
    binlog_path = /var/data # /var/data/binlog.001 etc will be created

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------+-----------------------------------+--------------------------------------+
| `Prev <conf-dist-threads.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-binlog-flush.html>`__   |
+--------------------------------------+-----------------------------------+--------------------------------------+
| 12.4.27. dist\_threads               | `Home <index.html>`__             |  12.4.29. binlog\_flush              |
+--------------------------------------+-----------------------------------+--------------------------------------+

.. raw:: html

   </div>
