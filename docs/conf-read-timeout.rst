.. raw:: html

   <div class="navheader">

12.4.5. read\_timeout
`Prev <conf-query-log-format.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-client-timeout.html>`__

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

.. rubric:: 12.4.5. read\_timeout
   :name: read_timeout
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Network client request read timeout, in seconds. Optional, default is 5
seconds. ``searchd`` will forcibly close the client connections which
fail to send a query within this timeout.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    read_timeout = 1

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+-----------------------------------+----------------------------------------+
| `Prev <conf-query-log-format.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-client-timeout.html>`__   |
+------------------------------------------+-----------------------------------+----------------------------------------+
| 12.4.4. query\_log\_format               | `Home <index.html>`__             |  12.4.6. client\_timeout               |
+------------------------------------------+-----------------------------------+----------------------------------------+

.. raw:: html

   </div>
