.. raw:: html

   <div class="navheader">

12.4.2. log
`Prev <conf-listen.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-query-log.html>`__

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

.. rubric:: 12.4.2. log
   :name: log
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Log file name. Optional, default is ‘searchd.log’. All ``searchd`` run
time events will be logged in this file.

Also you can use the ‘syslog’ as the file name. In this case the events
will be sent to syslog daemon. To use the syslog option the sphinx must
be configured ‘–with-syslog’ on building.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    log = /var/log/searchd.log

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------+-----------------------------------+-----------------------------------+
| `Prev <conf-listen.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-query-log.html>`__   |
+--------------------------------+-----------------------------------+-----------------------------------+
| 12.4.1. listen                 | `Home <index.html>`__             |  12.4.3. query\_log               |
+--------------------------------+-----------------------------------+-----------------------------------+

.. raw:: html

   </div>
