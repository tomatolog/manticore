.. raw:: html

   <div class="navheader">

12.4.38. watchdog
`Prev <conf-expansion-limit.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-sphinxql-state.html>`__

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

.. rubric:: 12.4.38. watchdog
   :name: watchdog
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Threaded server watchdog. Optional, default is 1 (watchdog enabled).
Introduced in version 2.0.1-beta.

A crashed query in ``threads`` multi-processing mode
(``workers = threads``) can take down the entire server. With watchdog
feature enabled, ``searchd`` additionally keeps a separate lightweight
process that monitors the main server process, and automatically
restarts the latter in case of abnormal termination. Watchdog is enabled
by default.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    watchdog = 0 # disable watchdog

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+-----------------------------------+----------------------------------------+
| `Prev <conf-expansion-limit.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-sphinxql-state.html>`__   |
+-----------------------------------------+-----------------------------------+----------------------------------------+
| 12.4.37. expansion\_limit               | `Home <index.html>`__             |  12.4.39. sphinxql\_state              |
+-----------------------------------------+-----------------------------------+----------------------------------------+

.. raw:: html

   </div>
