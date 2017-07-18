.. raw:: html

   <div class="navheader">

12.4.46. shutdown\_timeout
`Prev <conf-predicted-time-costs.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-ondisk-attrs-default.html>`__

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

.. rubric:: 12.4.46. shutdown\_timeout
   :name: shutdown_timeout
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

searchd –stopwait wait time, in seconds. Optional, default is 3 seconds.
Added in 2.2.1-beta.

When you run searchd –stopwait your daemon needs to perform some
activities before stopping like finishing queries, flushing RT RAM
chunk, flushing attributes and updating binlog. And it requires some
time. searchd –stopwait will wait up to shutdown\_time seconds for
daemon to finish its jobs. Suitable time depends on your index size and
load.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    shutdown_timeout = 5 # wait for up to 5 seconds

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------------+-----------------------------------+----------------------------------------------+
| `Prev <conf-predicted-time-costs.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-ondisk-attrs-default.html>`__   |
+----------------------------------------------+-----------------------------------+----------------------------------------------+
| 12.4.45. predicted\_time\_costs              | `Home <index.html>`__             |  12.4.47. ondisk\_attrs\_default             |
+----------------------------------------------+-----------------------------------+----------------------------------------------+

.. raw:: html

   </div>
