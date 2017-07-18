.. raw:: html

   <div class="navheader">

12.4.9. net\_workers
`Prev <conf-max-children.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-queue-max-length.html>`__

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

.. rubric:: 12.4.9. net\_workers
   :name: net_workers
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Number of network threads for workers=thread\_pool mode, default is 1.

Useful for extremely high query rates, when just 1 thread is not enough
to manage all the incoming queries.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------+-----------------------------------+------------------------------------------+
| `Prev <conf-max-children.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-queue-max-length.html>`__   |
+--------------------------------------+-----------------------------------+------------------------------------------+
| 12.4.8. max\_children                | `Home <index.html>`__             |  12.4.10. queue\_max\_length             |
+--------------------------------------+-----------------------------------+------------------------------------------+

.. raw:: html

   </div>
