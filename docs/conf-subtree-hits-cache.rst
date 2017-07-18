.. raw:: html

   <div class="navheader">

12.4.25. subtree\_hits\_cache
`Prev <conf-subtree-docs-cache.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-workers.html>`__

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

.. rubric:: 12.4.25. subtree\_hits\_cache
   :name: subtree_hits_cache
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Max common subtree hit cache size, per-query. Optional, default is 0
(disabled).

Limits RAM usage of a common subtree optimizer (see `Section 5.12,
“Multi-queries” <multi-queries.html>`__). At most this much RAM will be
spent to cache keyword occurrences (hits) per each query. Setting the
limit to 0 disables the optimizer.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    subtree_hits_cache = 16M

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+-----------------------------------+---------------------------------+
| `Prev <conf-subtree-docs-cache.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-workers.html>`__   |
+--------------------------------------------+-----------------------------------+---------------------------------+
| 12.4.24. subtree\_docs\_cache              | `Home <index.html>`__             |  12.4.26. workers               |
+--------------------------------------------+-----------------------------------+---------------------------------+

.. raw:: html

   </div>
