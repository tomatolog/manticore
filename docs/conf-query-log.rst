.. raw:: html

   <div class="navheader">

12.4.3. query\_log
`Prev <conf-log.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-query-log-format.html>`__

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

.. rubric:: 12.4.3. query\_log
   :name: query_log
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Query log file name. Optional, default is empty (do not log queries).
All search queries will be logged in this file. The format is described
in `Section 5.9, “\ ``searchd`` query log
formats” <query-log-format.html>`__.

In case of ‘plain’ format, you can use the ‘syslog’ as the path to the
log file. In this case all search queries will be sent to syslog daemon
with LOG\_INFO priority, prefixed with ‘[query]’ instead of timestamp.
To use the syslog option the sphinx must be configured ‘–with-syslog’ on
building.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    query_log = /var/log/query.log

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------+-----------------------------------+------------------------------------------+
| `Prev <conf-log.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-query-log-format.html>`__   |
+-----------------------------+-----------------------------------+------------------------------------------+
| 12.4.2. log                 | `Home <index.html>`__             |  12.4.4. query\_log\_format              |
+-----------------------------+-----------------------------------+------------------------------------------+

.. raw:: html

   </div>
