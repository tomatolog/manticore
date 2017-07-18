.. raw:: html

   <div class="navheader">

12.4.20. listen\_backlog
`Prev <conf-max-filter-values.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-read-buffer.html>`__

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

.. rubric:: 12.4.20. listen\_backlog
   :name: listen_backlog
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

TCP listen backlog. Optional, default is 5.

Windows builds currently (as of 0.9.9) can only process the requests one
by one. Concurrent requests will be enqueued by the TCP stack on OS
level, and requests that can not be enqueued will immediately fail with
“connection refused” message. listen\_backlog directive controls the
length of the connection queue. Non-Windows builds should work fine with
the default value.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    listen_backlog = 20

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+-----------------------------------+-------------------------------------+
| `Prev <conf-max-filter-values.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-read-buffer.html>`__   |
+-------------------------------------------+-----------------------------------+-------------------------------------+
| 12.4.19. max\_filter\_values              | `Home <index.html>`__             |  12.4.21. read\_buffer              |
+-------------------------------------------+-----------------------------------+-------------------------------------+

.. raw:: html

   </div>
