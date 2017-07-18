.. raw:: html

   <div class="navheader">

12.4.24. subtree\_docs\_cache
`Prev <conf-max-batch-queries.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-subtree-hits-cache.html>`__

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

.. rubric:: 12.4.24. subtree\_docs\_cache
   :name: subtree_docs_cache
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Max common subtree document cache size, per-query. Optional, default is
0 (disabled).

Limits RAM usage of a common subtree optimizer (see `Section 5.12,
“Multi-queries” <multi-queries.html>`__). At most this much RAM will be
spent to cache document entries per each query. Setting the limit to 0
disables the optimizer.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    subtree_docs_cache = 8M

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+-----------------------------------+--------------------------------------------+
| `Prev <conf-max-batch-queries.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-subtree-hits-cache.html>`__   |
+-------------------------------------------+-----------------------------------+--------------------------------------------+
| 12.4.23. max\_batch\_queries              | `Home <index.html>`__             |  12.4.25. subtree\_hits\_cache             |
+-------------------------------------------+-----------------------------------+--------------------------------------------+

.. raw:: html

   </div>
