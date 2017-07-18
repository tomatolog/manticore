.. raw:: html

   <div class="navheader">

12.4.23. max\_batch\_queries
`Prev <conf-read-unhinted.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-subtree-docs-cache.html>`__

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

.. rubric:: 12.4.23. max\_batch\_queries
   :name: max_batch_queries
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Limits the amount of queries per batch. Optional, default is 32.

Makes searchd perform a sanity check of the amount of the queries
submitted in a single batch when using
`multi-queries <multi-queries.html>`__. Set it to 0 to skip the check.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    max_batch_queries = 256

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+-----------------------------------+--------------------------------------------+
| `Prev <conf-read-unhinted.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-subtree-docs-cache.html>`__   |
+---------------------------------------+-----------------------------------+--------------------------------------------+
| 12.4.22. read\_unhinted               | `Home <index.html>`__             |  12.4.24. subtree\_docs\_cache             |
+---------------------------------------+-----------------------------------+--------------------------------------------+

.. raw:: html

   </div>
