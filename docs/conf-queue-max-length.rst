.. raw:: html

   <div class="navheader">

12.4.10. queue\_max\_length
`Prev <conf-net-workers.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-pid-file.html>`__

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

.. rubric:: 12.4.10. queue\_max\_length
   :name: queue_max_length
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Maximum pending queries queue length for workers=thread\_pool mode,
default is 0 (unlimited).

In case of high CPU load thread pool queries queue may grow all the
time. This directive lets you constrain queue length and start rejecting
incoming queries at some point with a “maxed out” message.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------+-----------------------------------+----------------------------------+
| `Prev <conf-net-workers.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-pid-file.html>`__   |
+-------------------------------------+-----------------------------------+----------------------------------+
| 12.4.9. net\_workers                | `Home <index.html>`__             |  12.4.11. pid\_file              |
+-------------------------------------+-----------------------------------+----------------------------------+

.. raw:: html

   </div>
